import os
from PIL import Image, ImageDraw, ImageFont

font_path = "C:\\Windows\\Fonts\\segoeuib.ttf"

def create_button(filename, text, subtext, bg_top, bg_bottom, border_color):
    width, height = 900, 220
    img = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # Shadow
    shadow_margin = 14
    draw.rounded_rectangle(
        [shadow_margin, shadow_margin + 12, width - shadow_margin, height - shadow_margin + 6],
        radius=55,
        fill=(0, 0, 0, 60)
    )

    # Gradient base simulation (pill button)
    btn_rect = [shadow_margin, shadow_margin, width - shadow_margin, height - shadow_margin - 8]
    # Draw border
    draw.rounded_rectangle(btn_rect, radius=55, fill=border_color)
    
    # Inner fill
    inner_rect = [btn_rect[0] + 4, btn_rect[1] + 4, btn_rect[2] - 4, btn_rect[3] - 4]
    draw.rounded_rectangle(inner_rect, radius=52, fill=bg_top)

    # Top highlight / gloss
    highlight_rect = [inner_rect[0] + 12, inner_rect[1] + 6, inner_rect[2] - 12, inner_rect[1] + 45]
    draw.rounded_rectangle(highlight_rect, radius=25, fill=(255, 255, 255, 75))

    # Triangle Play Icon on left
    icon_left = inner_rect[0] + 55
    icon_top = inner_rect[1] + 40
    icon_bottom = inner_rect[3] - 40
    icon_height = icon_bottom - icon_top
    tri_points = [
        (icon_left, icon_top),
        (icon_left + int(icon_height * 0.86), (icon_top + icon_bottom) // 2),
        (icon_left, icon_bottom)
    ]
    # Play icon shadow
    draw.polygon([(p[0], p[1] + 3) for p in tri_points], fill=(0, 0, 0, 50))
    draw.polygon(tri_points, fill=(255, 255, 255, 255))

    # Text
    main_font = ImageFont.truetype(font_path, 54)
    sub_font = ImageFont.truetype(font_path, 32)

    # Main text position
    text_x = icon_left + int(icon_height * 0.86) + 35
    text_y = inner_rect[1] + 28

    # Text shadow
    draw.text((text_x + 2, text_y + 3), text, font=main_font, fill=(0, 0, 0, 80))
    draw.text((text_x, text_y), text, font=main_font, fill=(255, 255, 255, 255))

    if subtext:
        sub_y = text_y + 68
        draw.text((text_x + 2, sub_y + 2), subtext, font=sub_font, fill=(0, 0, 0, 60))
        draw.text((text_x, sub_y), subtext, font=sub_font, fill=(255, 249, 196, 255))

    img.save(filename, "PNG")
    print(f"Created {filename}")

# Button 1: Thỏ tìm cà rốt (Cam)
create_button(
    "Nut_Play_Tho_Tim_Ca_Rot.png",
    "BẮT ĐẦU CHƠI",
    "Trò chơi: Giúp Thỏ Tìm Cà Rốt (Tổng = 10)",
    bg_top=(255, 122, 0, 255),
    bg_bottom=(220, 80, 0, 255),
    border_color=(255, 200, 100, 255)
)

# Button 2: Vườn xoài (Xanh lá - Vàng chanh)
create_button(
    "Nut_Play_Vuon_Xoai_Ky_Dieu.png",
    "BẮT ĐẦU CHƠI",
    "Trò chơi: Vườn Xoài Kỳ Diệu",
    bg_top=(46, 204, 113, 255),
    bg_bottom=(39, 174, 96, 255),
    border_color=(168, 230, 207, 255)
)

# Button 3: Nút Play chung gọn gàng
create_button(
    "Nut_Play_Chung.png",
    "BẮT ĐẦU CHƠI",
    "Bấm vào đây để mở trò chơi",
    bg_top=(52, 152, 219, 255),
    bg_bottom=(41, 128, 185, 255),
    border_color=(174, 214, 241, 255)
)


# Button 4: Game Hái Táo Về Giỏ (Đỏ tươi)
create_button(
    "Nut_Play_Hai_Tao.png",
    "BẮT ĐẦU CHƠI",
    "Trò chơi: Hái Táo Về Giỏ (Phép cộng 2 - 6)",
    bg_top=(235, 50, 50, 255),
    bg_bottom=(180, 25, 25, 255),
    border_color=(255, 170, 170, 255)
)
