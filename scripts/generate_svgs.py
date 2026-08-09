import os

def create_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"Created directory: {path}")

def save_svg(filepath, content):
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content.strip())
    print(f"Saved SVG to: {filepath}")

def main():
    img_dir = "img"
    create_directory(img_dir)

    # 1. Header Welcome Banner (Text & Sticker only, no embedded image to prevent animation freeze)
    header_welcome = """
<svg width="800" height="110" viewBox="0 0 800 110" fill="none" xmlns="http://www.w3.org/2000/svg">
  <style>
    .title { font-family: 'Arial Black', Impact, sans-serif; font-size: 32px; fill: #000000; font-weight: 900; letter-spacing: 0.5px; }
    .grid-dot { fill: #000000; opacity: 0.15; }
    .sticker-text { font-family: Arial, sans-serif; font-size: 11px; font-weight: bold; fill: #ffffff; }
  </style>
  <!-- Shadow -->
  <rect x="10" y="10" width="780" height="90" rx="8" fill="#000000" />
  <!-- Main Rect -->
  <rect x="4" y="4" width="780" height="90" rx="8" fill="#FFDE4D" stroke="#000000" stroke-width="4" />
  
  <!-- Dot Grid -->
  <g class="grid-dot">
    <circle cx="40" cy="43" r="3.5" /><circle cx="60" cy="43" r="3.5" /><circle cx="80" cy="43" r="3.5" />
    <circle cx="40" cy="58" r="3.5" /><circle cx="60" cy="58" r="3.5" /><circle cx="80" cy="58" r="3.5" />
    <circle cx="40" cy="73" r="3.5" /><circle cx="60" cy="73" r="3.5" /><circle cx="80" cy="73" r="3.5" />
  </g>
  
  <!-- Title Text -->
  <text x="110" y="60" class="title">HAWOO, GERRY DISINI 👋</text>
  
  <!-- Sticker -->
  <g transform="translate(650, 35)">
    <rect x="0" y="0" width="110" height="28" rx="6" fill="#FF4E88" stroke="#000000" stroke-width="2.5" />
    <text x="55" y="18" text-anchor="middle" class="sticker-text">STATUS: ACTIVE</text>
  </g>
</svg>
"""
    save_svg(os.path.join(img_dir, "header_welcome.svg"), header_welcome)

    # 2. Section Title Banners
    titles = {
        "title_about.svg": ("ABOUT ME", "#42F5B2"),
        "title_tools.svg": ("LANGUAGES &amp; TOOLS", "#00E5FF"),
        "title_stats.svg": ("MY STATS", "#FF4E88"),
        "title_chill.svg": ("PLAY &amp; CHILL", "#FF8E2B")
    }

    for filename, (text, color) in titles.items():
        title_svg = f"""
<svg width="320" height="60" viewBox="0 0 320 60" fill="none" xmlns="http://www.w3.org/2000/svg">
  <style>
    .title-text {{ font-family: Arial, sans-serif; font-size: 18px; font-weight: 900; fill: #000000; letter-spacing: 0.5px; }}
  </style>
  <rect x="8" y="8" width="304" height="44" rx="6" fill="#000000" />
  <rect x="3" y="3" width="304" height="44" rx="6" fill="{color}" stroke="#000000" stroke-width="3" />
  <text x="20" y="31" class="title-text">{text}</text>
</svg>
"""
        save_svg(os.path.join(img_dir, filename), title_svg)

    # 3. Social Badges
    socials = {
        "badge_linkedin.svg": ("LinkedIn", "#00E5FF", '<path d="M2 17h3V8H2v9zM3.5 6.5c1 0 1.7-.7 1.7-1.7S4.5 3 3.5 3 1.8 3.8 1.8 4.8s.7 1.7 1.7 1.7zm13.5 10.5h-3v-5.5c0-1.3-.5-2-1.5-2s-1.7.7-1.7 2v5.5h-3v-9h3v1.3c.4-.7 1.2-1.3 2.5-1.3 2.5 0 3.7 1.6 3.7 4V17z" fill="#000000"/>'),
        "badge_youtube.svg": ("YouTube", "#FE5E5E", '<path d="M19.5 5.8c-.2-.8-.9-1.5-1.8-1.7C16 3.7 10 3.7 10 3.7s-6 0-7.7.4c-.9.2-1.6.9-1.8 1.7C.1 7.5.1 10 .1 10s0 2.5.4 4.2c.2.8.9 1.5 1.8 1.7 1.7.4 7.7.4 7.7.4s6 0 7.7-.4c.9-.2 1.6-.9 1.8-1.7.4-1.7.4-4.2.4-4.2s0-2.5-.4-4.2zM8 13.5v-7l5.5 3.5-5.5 3.5z" fill="#000000"/>'),
        "badge_instagram.svg": ("Instagram", "#FF4E88", '<path d="M10 5.2c1.6 0 1.7 0 2.4.1.6 0 1 .1 1.2.2.3.1.6.3.8.5.2.2.4.5.5.8.1.2.2.6.2 1.2 0 .7.1.8.1 2.4s0 1.7-.1 2.4c0 .6-.1 1-.2 1.2-.1.3-.3.6-.5.8-.2.2-.5.4-.8.5-.2.1-.6.2-1.2.2-.7 0-.8.1-2.4.1s-1.7 0-2.4-.1c-.6 0-1-.1-1.2-.2-.3-.1-.6-.3-.8-.5-.2-.2-.4-.5-.5-.8-.1-.2-.2-.6-.2-1.2 0-.7-.1-.8-.1-2.4s0-1.7.1-2.4c0-.6.1-1 .2-1.2.1-.3.3-.6.5-.8.2-.2.5-.4.8-.5.2-.1.6-.2 1.2-.2.7 0 .8-.1 2.4-.1zm0-1.8c-1.6 0-1.8 0-2.4.1-.7 0-1.2.1-1.6.3-.4.2-.8.4-1.1.8-.4.4-.6.7-.8 1.1-.2.4-.3.9-.3 1.6-.1.6-.1.8-.1 2.4s0 1.8.1 2.4c0 .7.1 1.2.3 1.6.2.4.4.8.8 1.1.4.4.7.6 1.1.8.4.2.9.3 1.6.3.6.1.8.1 2.4.1s1.8 0 2.4-.1c.7 0 1.2-.1 1.6-.3.4-.2.8-.4 1.1-.8.4-.4.6-.7.8-1.1.2-.4.3-.9.3-1.6.1-.6.1-.8.1-2.4s0-1.8-.1-2.4c0-.7-.1-1.2-.3-1.6-.2-.4-.4-.8-.8-1.1-.4-.4-.7-.6-.1.1z M10 7.8c-1.2 0-2.2 1-2.2 2.2s1 2.2 2.2 2.2 2.2-1 2.2-2.2-1-2.2-2.2-2.2zm0 3.1c-.5 0-.9-.4-.9-.9s.4-.9.9-.9.9.4.9.9-.4.9-.9.9zm4.7-4.4c0 .3-.3.6-.6.6s-.6-.3-.6-.6.3-.6.6-.6.6.3.6.6z" fill="#000000"/>')
    }

    for filename, (label, color, path_data) in socials.items():
        social_svg = f"""
<svg width="150" height="42" viewBox="0 0 150 42" fill="none" xmlns="http://www.w3.org/2000/svg">
  <style>
    .label {{ font-family: Arial, sans-serif; font-size: 14px; font-weight: bold; fill: #000000; }}
  </style>
  <rect x="5" y="5" width="138" height="30" rx="6" fill="#000000" />
  <rect x="2" y="2" width="138" height="30" rx="6" fill="{color}" stroke="#000000" stroke-width="2.5" />
  <g transform="translate(15, 7)">
    <svg width="20" height="20" viewBox="0 0 20 20">
      {path_data}
    </svg>
    <text x="28" y="15" class="label">{label}</text>
  </g>
</svg>
"""
        save_svg(os.path.join(img_dir, filename), social_svg)

    # 4. Unified Tech Stack Grid SVG
    tech_stack = """
<svg width="760" height="120" viewBox="0 0 760 120" fill="none" xmlns="http://www.w3.org/2000/svg">
  <style>
    .label { font-family: Arial, sans-serif; font-size: 13px; font-weight: bold; fill: #000000; }
  </style>
  
  <!-- Row 1: HTML5, CSS3, Bootstrap -->
  <!-- HTML5 -->
  <g transform="translate(10, 10)">
    <rect x="4" y="4" width="226" height="42" rx="6" fill="#000000" />
    <rect x="0" y="0" width="226" height="42" rx="6" fill="#FF6B6B" stroke="#000000" stroke-width="2.5" />
    <g transform="translate(15, 11)">
      <svg width="20" height="20" viewBox="0 0 20 20">
        <path d="M1.5 1.5l1.3 12.3 5.7 1.6 5.7-1.6 1.3-12.3H1.5zm9.6 4.3l-.2 1.6H5.6l.1.8h4.7l-.3 3.3-3.2.9-3.2-.9-.2-2h1.4l.1 1 1.8.5 1.8-.5.2-1.6H3.6l-.4-3.7h7.5z" fill="#000000"/>
      </svg>
      <text x="26" y="14" class="label">HTML5</text>
    </g>
  </g>

  <!-- CSS3 -->
  <g transform="translate(262, 10)">
    <rect x="4" y="4" width="226" height="42" rx="6" fill="#000000" />
    <rect x="0" y="0" width="226" height="42" rx="6" fill="#4D96FF" stroke="#000000" stroke-width="2.5" />
    <g transform="translate(15, 11)">
      <svg width="20" height="20" viewBox="0 0 20 20">
        <path d="M1.5 1.5l1.3 12.3 5.7 1.6 5.7-1.6 1.3-12.3H1.5zm9.6 4.3l-.2 1.6H5.6l.1.8h4.7l-.3 3.3-3.2.9-3.2-.9-.2-2h1.4l.1 1 1.8.5 1.8-.5.2-1.6H3.6l-.4-3.7h7.5z" fill="#000000"/>
      </svg>
      <text x="26" y="14" class="label">CSS3</text>
    </g>
  </g>

  <!-- Bootstrap -->
  <g transform="translate(514, 10)">
    <rect x="4" y="4" width="226" height="42" rx="6" fill="#000000" />
    <rect x="0" y="0" width="226" height="42" rx="6" fill="#BC7AF9" stroke="#000000" stroke-width="2.5" />
    <g transform="translate(15, 11)">
      <svg width="20" height="20" viewBox="0 0 20 20">
        <path d="M2 2h7.2c1.6 0 2.8.6 2.8 2 0 1-.6 1.6-1.6 1.8.6.3 1.2.9 1.2 1.8 0 1.6-1.2 2.4-2.8 2.4H2V2zm2.4 2v1.6H8c.6 0 1-.2 1-.8s-.4-.8-1-.8H4.4zm0 3.6V9H8.4c.6 0 1-.3 1-1s-.4-1-1-1H4.4z" fill="#000000"/>
      </svg>
      <text x="26" y="14" class="label">Bootstrap</text>
    </g>
  </g>

  <!-- Row 2: PHP, Laravel, Photoshop -->
  <!-- PHP -->
  <g transform="translate(10, 65)">
    <rect x="4" y="4" width="226" height="42" rx="6" fill="#000000" />
    <rect x="0" y="0" width="226" height="42" rx="6" fill="#8F43EE" stroke="#000000" stroke-width="2.5" />
    <g transform="translate(15, 11)">
      <svg width="20" height="20" viewBox="0 0 20 20">
        <path d="M4 11l-1 4H1l2.5-10H6l-.8 3h1.8L7.8 5h2.5L7.8 15h-2.5l1.2-5H4.2zm6 1c0-2 1.5-3.5 3.5-3.5S17 10 17 12s-1.5 3.5-3.5 3.5-3.5-1.5-3.5-3.5zm2.2 0c0 .8.5 1.3 1.3 1.3s1.3-.5 1.3-1.3-.5-1.3-1.3-1.3-1.3.5-1.3 1.3zm6.3-4.5H21L20.2 11h1.8l-.8 4H18.7l2.5-10z" fill="#000000"/>
      </svg>
      <text x="26" y="14" class="label">PHP</text>
    </g>
  </g>

  <!-- Laravel -->
  <g transform="translate(262, 65)">
    <rect x="4" y="4" width="226" height="42" rx="6" fill="#000000" />
    <rect x="0" y="0" width="226" height="42" rx="6" fill="#FF4B4B" stroke="#000000" stroke-width="2.5" />
    <g transform="translate(15, 11)">
      <svg width="20" height="20" viewBox="0 0 20 20">
        <path d="M2.5 10.5l5.5-3.2 5.5 3.2v6.3l-5.5 3.2-5.5-3.2v-6.3zm5.5 1.5L4.5 10v4.7l3.5 2 3.5-2V10L8 12z" fill="#000000"/>
      </svg>
      <text x="26" y="14" class="label">Laravel</text>
    </g>
  </g>

  <!-- Photoshop -->
  <g transform="translate(514, 65)">
    <rect x="4" y="4" width="226" height="42" rx="6" fill="#000000" />
    <rect x="0" y="0" width="226" height="42" rx="6" fill="#00C4FF" stroke="#000000" stroke-width="2.5" />
    <g transform="translate(15, 11)">
      <svg width="20" height="20" viewBox="0 0 20 20">
        <path d="M2.5 2.5h15v15h-15v-15zm4 4v7.5h2.5v-2.5h1.5c1.2 0 2-1 2-2.5s-.8-2.5-2-2.5H6.5zm2.5 2v1.5h1c.4 0 .7-.3.7-.7s-.3-.8-.7-.8h-1zm4.5 1.7c0 1.2.6 1.8 1.8 1.8.6 0 1-.3 1-.3v-1.2s-.3.2-.6.2c-.4 0-.6-.3-.6-.8v-2h1.2v-1.2h-1.2V7.5h-1.2v1.5h-.6v1.2h.6v2z" fill="#000000"/>
      </svg>
      <text x="26" y="14" class="label">Photoshop</text>
    </g>
  </g>
</svg>
"""
    save_svg(os.path.join(img_dir, "tech_stack.svg"), tech_stack)

if __name__ == "__main__":
    main()
