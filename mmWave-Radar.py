
# File: 'pygame_radar.py'
import math
import time
import serial
import pygame
import serial_protocol

# --- Config ---
PORT = '/dev/ttyUSB2'
BAUD = 256000
SER_TIMEOUT_S = 0.03

WINDOW_SIZE = (900, 700)
MAX_RANGE_MM = 6000          # radar radius in mm
READS_PER_FRAME = 5
FPS = 60

# If your sensor reports forward as negative Y, set True (HLK-LD2450 often does)
FORWARD_Y_IS_NEGATIVE = True

def sensor_to_display(x_mm, y_mm):
    # Convert sensor coords to display coords (display Y up)
    y_disp = -y_mm if FORWARD_Y_IS_NEGATIVE else y_mm
    return float(x_mm), float(y_disp)

def to_screen(center, scale, x_mm, y_mm):
    return int(center[0] + x_mm * scale), int(center[1] - y_mm * scale)

def main():
    ser = serial.Serial(PORT, BAUD, timeout=SORT_TIMEOUT_S) if (SORT_TIMEOUT_S := SER_TIMEOUT_S) else serial.Serial(PORT, BAUD, timeout=SER_TIMEOUT_S)

    pygame.init()
    screen = pygame.display.set_mode(WINDOW_SIZE)
    pygame.display.set_caption('Front 180° Radar (PyGame)')
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 18)

    # Geometry: sensor at bottom center; semicircle fits top with margins
    top_margin = 20
    side_margin = 20
    bottom_margin = 40
    center = (WINDOW_SIZE[0] // 2, WINDOW_SIZE[1] - bottom_margin)
    radius_px = min(center[1] - top_margin, WINDOW_SIZE[0] // 2 - side_margin)
    scale = radius_px / float(MAX_RANGE_MM)

    blips = []  # (x_d, y_d, ts)

    running = True
    try:
        while running:
            for e in pygame.event.get():
                if e.type == pygame.QUIT or (e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE):
                    running = False

            # Read multiple frames per tick
            for _ in range(READS_PER_FRAME):
                frame = ser.read_until(serial_protocol.REPORT_TAIL)
                if not frame or serial_protocol.REPORT_HEADER not in frame:
                    continue
                vals = serial_protocol.read_radar_data(frame)
                if vals is None or len(vals) < 12:
                    continue

                now = time.time()
                # Unpack three targets: (x, y, speed, dist)
                for i in range(3):
                    base = i * 4
                    sx = vals[base + 0]
                    sy = vals[base + 1]
                    spd = vals[base + 2]
                    if sx == 0 and sy == 0 and spd == 0:
                        continue

                    xd, yd = sensor_to_display(sx, sy)

                    # Front hemisphere only (top)
                    if yd < 0:
                        continue

                    # Clip to range
                    if math.hypot(xd, yd) > MAX_RANGE_MM * 1.02:
                        continue

                    blips.append((xd, yd, now))

            # Decay old blips (simple fade trail)
            now = time.time()
            lifetime_s = 1.2
            blips = [b for b in blips if now - b[2] <= lifetime_s]

            # Draw
            screen.fill((0, 0, 0))

            # Range rings (upper semicircle)
            for frac in (0.2, 0.4, 0.6, 0.8, 1.0):
                r = int(radius_px * frac)
                rect = pygame.Rect(center[0] - r, center[1] - r, 2 * r, 2 * r)
                pygame.draw.arc(screen, (50, 50, 50), rect, 0, 2 * math.pi, 1)

            # Baseline at sensor
            pygame.draw.line(screen, (70, 70, 70),
                             (center[0] - radius_px, center[1]),
                             (center[0] + radius_px, center[1]), 1)


            # Blips with fade
            for xd, yd, ts in blips:
                age = now - ts
                fade = max(0.0, 1.0 - age / lifetime_s)
                color = (0, int(120 + 135 * fade), 0)
                sx, sy = to_screen(center, scale, xd, yd)
                pygame.draw.circle(screen, color, (sx, sy), max(3, int(6 * fade)))

            hud = font.render(f'Port:{PORT}  Range:{MAX_RANGE_MM}mm  Scale:{scale:.3f}px/mm  Blips:{len(blips)}',
                              True, (200, 200, 200))
            screen.blit(hud, (10, 10))

            pygame.display.flip()
            clock.tick(FPS)
    finally:
        try:
            ser.close()
        except Exception:
            pass
        pygame.quit()

if __name__ == '__main__':
    main()
