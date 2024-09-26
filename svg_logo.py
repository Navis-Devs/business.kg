import cairosvg

svg_content = '''<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">

<!-- Uploaded to: SVG Repo, www.svgrepo.com, Transformed by: SVG Repo Mixer Tools -->
<svg width="256px" height="256px" viewBox="-0.24 -0.24 24.48 24.48" fill="none" xmlns="http://www.w3.org/2000/svg">

<g id="SVGRepo_bgCarrier" stroke-width="0">

<rect x="-0.24" y="-0.24" width="24.48" height="24.48" rx="0" fill="#1b4dfc" strokewidth="0"/>

</g>

<g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"/>

<g id="SVGRepo_iconCarrier"> <path d="M10 8H14C15.1046 8 16 8.89543 16 10C16 11.1046 15.1046 12 14 12M10 8V12M10 8H8.5M10 8V6.5M14 12H10M14 12C15.1046 12 16 12.8954 16 14C16 15.1046 15.1046 16 14 16H10M10 12V16M10 16H8.5M10 16V17.5M13 8V6.5M13 17.5V16M21 12C21 16.9706 16.9706 21 12 21C7.02944 21 3 16.9706 3 12C3 7.02944 7.02944 3 12 3C16.9706 3 21 7.02944 21 12Z" stroke="#ffffff" stroke-width="1.7280000000000002" stroke-linecap="round" stroke-linejoin="round"/> </g>

</svg>'''

cairosvg.svg2png(bytestring=svg_content, write_to="logo.png", output_width=1920, output_height=1080)

print("SVG успешно преобразован в PNG")
