import os
from PIL import Image, ImageDraw, ImageFilter

def create_svg_favicon():
    svg_content = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="64" height="64">
  <defs>
    <!-- Brand Gradient: Deli Crimson to Warm Apricot -->
    <linearGradient id="brandGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#e63946"/>
      <stop offset="100%" stop-color="#f4a261"/>
    </linearGradient>

    <!-- Top Bun Golden Toast Gradient -->
    <linearGradient id="bunGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#ffebaa"/>
      <stop offset="50%" stop-color="#f6ba5d"/>
      <stop offset="100%" stop-color="#d9822b"/>
    </linearGradient>

    <!-- Bottom Bun Gradient -->
    <linearGradient id="bottomBunGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#f6ba5d"/>
      <stop offset="100%" stop-color="#c9701d"/>
    </linearGradient>

    <!-- Tomato Gradient -->
    <linearGradient id="tomatoGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#ef233c"/>
      <stop offset="100%" stop-color="#ba181b"/>
    </linearGradient>

    <!-- Melted Cheddar Gradient -->
    <linearGradient id="cheeseGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ffea79"/>
      <stop offset="100%" stop-color="#ff9e00"/>
    </linearGradient>

    <!-- Deli Patty / Roast Beef Layer Gradient -->
    <linearGradient id="meatGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#7d4421"/>
      <stop offset="100%" stop-color="#4d240e"/>
    </linearGradient>

    <!-- Crisp Lettuce Gradient -->
    <linearGradient id="lettuceGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#70e000"/>
      <stop offset="50%" stop-color="#38b000"/>
      <stop offset="100%" stop-color="#1b6302"/>
    </linearGradient>

    <filter id="shadow" x="-10%" y="-10%" width="120%" height="130%">
      <feDropShadow dx="0" dy="1.5" stdDeviation="1.2" flood-color="#000000" flood-opacity="0.3"/>
    </filter>
  </defs>

  <!-- Circular Brand Badge (Matches .logo-icon in navbar) -->
  <circle cx="32" cy="32" r="30" fill="url(#brandGrad)"/>
  <!-- Crisp inner highlight ring for high-contrast on all light & dark browser tabs -->
  <circle cx="32" cy="32" r="29.25" fill="none" stroke="#ffffff" stroke-width="1.5" stroke-opacity="0.4"/>

  <!-- Gourmet Layered Sandwich Icon -->
  <g filter="url(#shadow)">
    <!-- 1. Bottom Bun -->
    <path d="M 16 42 C 16 40 18 39.5 20 39.5 L 44 39.5 C 46 39.5 48 40 48 42 C 48 46.5 41 48 32 48 C 23 48 16 46.5 16 42 Z" fill="url(#bottomBunGrad)" stroke="#9c4e09" stroke-width="0.75"/>

    <!-- 2. Savory Patty / Deli Meat -->
    <rect x="14" y="36.5" width="36" height="4.5" rx="2.25" fill="url(#meatGrad)"/>

    <!-- 3. Melted Cheddar Slice with Delicious Pointed Drip -->
    <path d="M 14 34.5 L 50 34.5 L 48 37 L 39 37 L 33 42.5 L 27 37 L 16 37 Z" fill="url(#cheeseGrad)"/>

    <!-- 4. Fresh Crisp Lettuce Leaf with Wavy Ruffles -->
    <path d="M 12 32 C 14.5 29.5 17.5 33 21 31 C 24 29 27 32.5 30 31 C 33 29.5 36 32.5 39 31 C 42 29.5 45 32.5 48.5 30.5 C 51 30 52.5 32 51.5 33.5 C 49 35.5 15 35.5 12 32 Z" fill="url(#lettuceGrad)"/>

    <!-- 5. Fresh Tomato Slices -->
    <rect x="17" y="28" width="13" height="3.2" rx="1.6" fill="url(#tomatoGrad)"/>
    <rect x="34" y="28" width="13" height="3.2" rx="1.6" fill="url(#tomatoGrad)"/>

    <!-- 6. Golden Toasted Top Bun Dome -->
    <path d="M 14.5 28 C 14.5 18.5 21.5 15.5 32 15.5 C 42.5 15.5 49.5 18.5 49.5 28 C 49.5 29 48 29.5 46.5 29.5 L 17.5 29.5 C 16 29.5 14.5 29 14.5 28 Z" fill="url(#bunGrad)" stroke="#a85910" stroke-width="0.75"/>

    <!-- 7. White Sesame Seeds -->
    <ellipse cx="25" cy="21" rx="1.1" ry="0.65" fill="#fffdf5" transform="rotate(-15 25 21)"/>
    <ellipse cx="32" cy="19" rx="1.1" ry="0.65" fill="#fffdf5"/>
    <ellipse cx="39" cy="21.5" rx="1.1" ry="0.65" fill="#fffdf5" transform="rotate(20 39 21.5)"/>
    <ellipse cx="28.5" cy="24.5" rx="1" ry="0.55" fill="#fffdf5" transform="rotate(10 28.5 24.5)"/>
    <ellipse cx="35.5" cy="24.5" rx="1" ry="0.55" fill="#fffdf5" transform="rotate(-10 35.5 24.5)"/>
  </g>
</svg>
'''
    with open("favicon.svg", "w", encoding="utf-8") as f:
        f.write(svg_content.strip() + "\n")
    print("Created favicon.svg successfully")

def create_raster_favicons():
    # Render at 512x512 with 4x supersampling (2048x2048) or 1024x1024 for ultra-smooth edges
    size = 1024
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    cx, cy = size // 2, size // 2
    r = int(size * 0.47)

    # 1. Outer circle with gradient interpolation (#e63946 to #f4a261)
    # 135-degree linear gradient
    c1 = (230, 57, 70)   # #e63946
    c2 = (244, 162, 97)  # #f4a261
    
    # Create gradient badge mask
    badge_mask = Image.new("L", (size, size), 0)
    badge_mask_draw = ImageDraw.Draw(badge_mask)
    badge_mask_draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=255)

    grad = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    for y in range(size):
        for x in range(size):
            # calculate diagonal progression 0..1
            t = (x + y) / (2.0 * size)
            t = max(0.0, min(1.0, t))
            r_c = int(c1[0] + (c2[0] - c1[0]) * t)
            g_c = int(c1[1] + (c2[1] - c1[1]) * t)
            b_c = int(c1[2] + (c2[2] - c1[2]) * t)
            grad.putpixel((x, y), (r_c, g_c, b_c, 255))
    
    img.paste(grad, (0, 0), badge_mask)

    # Inner highlight ring for contrast
    draw = ImageDraw.Draw(img)
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], outline=(255, 255, 255, 90), width=int(size * 0.024))

    # Scale factor from 64-grid to size
    s = size / 64.0

    # Helper function to map (x, y) coordinates from 64x64 grid
    def pt(x, y):
        return (x * s, y * s)

    # Sandwich parts:
    # 1. Bottom Bun:
    # M 16 42 C 16 40 18 39.5 20 39.5 L 44 39.5 C 46 39.5 48 40 48 42 C 48 46.5 41 48 32 48 C 23 48 16 46.5 16 42 Z
    bottom_bun_box = [pt(16, 39.5)[0], pt(16, 39.5)[1], pt(48, 48)[0], pt(48, 48)[1]]
    draw.rounded_rectangle([pt(16, 39.5)[0], pt(16, 39.5)[1], pt(48, 47.5)[0], pt(48, 47.5)[1]], 
                           radius=int(4 * s), fill=(244, 180, 93, 255), outline=(170, 90, 20, 255), width=max(1, int(0.75 * s)))

    # 2. Savory Patty
    draw.rounded_rectangle([pt(14, 36.5)[0], pt(14, 36.5)[1], pt(50, 41)[0], pt(50, 41)[1]],
                           radius=int(2.25 * s), fill=(105, 52, 22, 255))

    # 3. Melted Cheddar Slice with pointed drip
    cheese_pts = [
        pt(14, 34.5), pt(50, 34.5), pt(48, 37), pt(39, 37),
        pt(33, 43), pt(27, 37), pt(16, 37)
    ]
    draw.polygon(cheese_pts, fill=(255, 195, 15, 255))

    # 4. Lettuce ruffles
    lettuce_pts = [
        pt(12, 32.5), pt(15, 30.5), pt(18, 33), pt(21, 31),
        pt(24, 29.5), pt(27, 32.5), pt(30, 31), pt(33, 29.5),
        pt(36, 32.5), pt(39, 31), pt(42, 29.5), pt(45, 32.5),
        pt(48.5, 30.5), pt(51.5, 33), pt(50, 35.5), pt(14, 35.5)
    ]
    draw.polygon(lettuce_pts, fill=(60, 185, 20, 255))

    # 5. Tomato slices
    draw.rounded_rectangle([pt(17, 28)[0], pt(17, 28)[1], pt(30, 31.5)[0], pt(30, 31.5)[1]],
                           radius=int(1.6 * s), fill=(230, 40, 55, 255))
    draw.rounded_rectangle([pt(34, 28)[0], pt(34, 28)[1], pt(47, 31.5)[0], pt(47, 31.5)[1]],
                           radius=int(1.6 * s), fill=(230, 40, 55, 255))

    # 6. Top Bun Dome
    # Ellipse/arc dome from 14.5 to 49.5, y from 15.5 to 29.5
    top_bun_mask = Image.new("L", (size, size), 0)
    top_mask_draw = ImageDraw.Draw(top_bun_mask)
    top_mask_draw.ellipse([pt(14.5, 15.5)[0], pt(14.5, 15.5)[1], pt(49.5, 42)[0], pt(49.5, 42)[1]], fill=255)
    top_mask_draw.rectangle([0, int(29.5 * s), size, size], fill=0)

    top_bun_layer = Image.new("RGBA", (size, size), (248, 190, 95, 255))
    img.paste(top_bun_layer, (0, 0), top_bun_mask)

    draw = ImageDraw.Draw(img)
    # Top bun outline
    draw.arc([pt(14.5, 15.5)[0], pt(14.5, 15.5)[1], pt(49.5, 42)[0], pt(49.5, 42)[1]],
             start=180, end=360, fill=(185, 95, 15, 255), width=max(1, int(0.75 * s)))
    draw.line([pt(14.5, 29.5), pt(49.5, 29.5)], fill=(185, 95, 15, 255), width=max(1, int(0.75 * s)))

    # 7. Sesame seeds
    seeds = [
        (25, 21, 1.2, 0.7),
        (32, 19, 1.2, 0.7),
        (39, 21.5, 1.2, 0.7),
        (28.5, 24.5, 1.0, 0.6),
        (35.5, 24.5, 1.0, 0.6)
    ]
    for sx, sy, rx, ry in seeds:
        draw.ellipse([pt(sx - rx, sy - ry)[0], pt(sx - rx, sy - ry)[1],
                      pt(sx + rx, sy + ry)[0], pt(sx + rx, sy + ry)[1]],
                     fill=(255, 253, 245, 255))

    # Save multi-size icons
    img_16 = img.resize((16, 16), Image.Resampling.LANCZOS)
    img_32 = img.resize((32, 32), Image.Resampling.LANCZOS)
    img_48 = img.resize((48, 48), Image.Resampling.LANCZOS)
    img_180 = img.resize((180, 180), Image.Resampling.LANCZOS)
    img_192 = img.resize((192, 192), Image.Resampling.LANCZOS)

    img_16.save("favicon-16x16.png", "PNG")
    img_32.save("favicon-32x32.png", "PNG")
    img_180.save("apple-touch-icon.png", "PNG")
    img_192.save("favicon-192x192.png", "PNG")
    
    # Save standard .ico containing 16, 32, 48
    img.save("favicon.ico", format="ICO", sizes=[(16, 16), (32, 32), (48, 48)])
    print("Created favicon.ico, favicon-32x32.png, favicon-16x16.png, apple-touch-icon.png successfully")

if __name__ == "__main__":
    create_svg_favicon()
    create_raster_favicons()
