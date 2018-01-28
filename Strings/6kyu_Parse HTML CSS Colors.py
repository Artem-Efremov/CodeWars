"""
In this kata you parse RGB colors represented by strings. The formats are primarily used in HTML and CSS. Your task is to implement a function which takes a color as a string and returns the parsed color as a map (see Examples).
Input:

The input string represents one of the following:

    6-digit hexadecimal - "#RRGGBB"
    e.g. "#012345", "#789abc", "#FFA077"
    Each pair of digits represents a value of the channel in hexadecimal: 00 to FF

    3-digit hexadecimal - "#RGB"
    e.g. "#012", "#aaa", "#F5A"
    Each digit represents a value 0 to F which translates to 2-digit hexadecimal: 0->00, 1->11, 2->22, and so on.

    Preset color name
    e.g. "red", "BLUE", "LimeGreen"
    You have to use the predefined map PRESET_COLORS (JavaScript, Python, Ruby), presetColors (Java, C#, Haskell), or preset-colors (Clojure). The keys are the names of preset colors in lower-case and the values are the corresponding colors in 6-digit hexadecimal (same as 1. "#RRGGBB").

Examples:

parse_html_color('#80FFA0')   # => {'r': 128, 'g': 255, 'b': 160}
parse_html_color('#3B7')      # => {'r': 51,  'g': 187, 'b': 119}
parse_html_color('LimeGreen') # => {'r': 50,  'g': 205, 'b': 50 }


"""

def parse_html_color(col):
    
    def read_color(col):
        if col[0] == '#' and len(col) == 4:
            return three_to_six_hex(col[1:])
        elif col[0] == '#' and len(col) == 7:
            return six_hex_to_dec(col[1:])
        else:
            return preset_to_hex(col)
    
    def preset_to_hex(col):
        return six_hex_to_dec(PRESET_COLORS.get(col.lower())[1:])

    def three_to_six_hex(col):
        return six_hex_to_dec(''.join([i*2 for i in col]))
        
    def six_hex_to_dec(col):
        r = int(col[:2], 16)
        g = int(col[2:4], 16)
        b = int(col[4:], 16)
        return represent(r, g, b)
                   
    def represent(r, g, b):
        return {'r': r, 'g': g, 'b': b}
    
    return read_color(col)



# PRESET_COLORS = {'rebeccapurple': '#663399', 'gainsboro': '#dcdcdc', 'darkslategrey': '#2f4f4f', 'floralwhite': '#fffaf0', 'crimson': '#dc143c', 'darkgreen': '#006400', 'chocolate': '#d2691e', 'white': '#ffffff', 'khaki': '#f0e68c', 'coral': '#ff7f50', 'slategray': '#708090', 'blueviolet': '#8a2be2', 'mediumaquamarine': '#66cdaa', 'turquoise': '#40e0d0', 'lightgrey': '#d3d3d3', 'salmon': '#fa8072', 'dimgrey': '#696969', 'mediumblue': '#0000cd', 'lightyellow': '#ffffe0', 'lightskyblue': '#87cefa', 'ghostwhite': '#f8f8ff', 'papayawhip': '#ffefd5', 'chartreuse': '#7fff00', 'lemonchiffon': '#fffacd', 'olivedrab': '#6b8e23', 'lime': '#00ff00', 'lightcoral': '#f08080', 'magenta': '#ff00ff', 'lightpink': '#ffb6c1', 'cornsilk': '#fff8dc', 'darkorchid': '#9932cc', 'grey': '#808080', 'ivory': '#fffff0', 'mediumorchid': '#ba55d3', 'linen': '#faf0e6', 'blue': '#0000ff', 'lightslategray': '#778899', 'forestgreen': '#228b22', 'yellow': '#ffff00', 'silver': '#c0c0c0', 'dodgerblue': '#1e90ff', 'deeppink': '#ff1493', 'whitesmoke': '#f5f5f5', 'lawngreen': '#7cfc00', 'powderblue': '#b0e0e6', 'cadetblue': '#5f9ea0', 'slategrey': '#708090', 'snow': '#fffafa', 'rosybrown': '#bc8f8f', 'goldenrod': '#daa520', 'mistyrose': '#ffe4e1', 'seashell': '#fff5ee', 'palevioletred': '#db7093', 'honeydew': '#f0fff0', 'oldlace': '#fdf5e6', 'gray': '#808080', 'pink': '#ffc0cb', 'midnightblue': '#191970', 'thistle': '#d8bfd8', 'seagreen': '#2e8b57', 'darkorange': '#ff8c00', 'skyblue': '#87ceeb', 'lightslategrey': '#778899', 'plum': '#dda0dd', 'gold': '#ffd700', 'lightsteelblue': '#b0c4de', 'black': '#000000', 'purple': '#800080', 'antiquewhite': '#faebd7', 'tan': '#d2b48c', 'olive': '#808000', 'peru': '#cd853f', 'palegreen': '#98fb98', 'mediumspringgreen': '#00fa9a', 'darkseagreen': '#8fbc8f', 'lightgoldenrodyellow': '#fafad2', 'mediumslateblue': '#7b68ee', 'mediumvioletred': '#c71585', 'hotpink': '#ff69b4', 'darkkhaki': '#bdb76b', 'aquamarine': '#7fffd4', 'slateblue': '#6a5acd', 'lavender': '#e6e6fa', 'azure': '#f0ffff', 'lightseagreen': '#20b2aa', 'mintcream': '#f5fffa', 'cyan': '#00ffff', 'aqua': '#00ffff', 'darkgrey': '#a9a9a9', 'darkolivegreen': '#556b2f', 'lightgray': '#d3d3d3', 'dimgray': '#696969', 'darkred': '#8b0000', 'darkblue': '#00008b', 'darkgoldenrod': '#b8860b', 'red': '#ff0000', 'beige': '#f5f5dc', 'greenyellow': '#adff2f', 'firebrick': '#b22222', 'darksalmon': '#e9967a', 'lavenderblush': '#fff0f5', 'lightsalmon': '#ffa07a', 'paleturquoise': '#afeeee', 'wheat': '#f5deb3', 'darkmagenta': '#8b008b', 'burlywood': '#deb887', 'darkcyan': '#008b8b', 'mediumturquoise': '#48d1cc', 'tomato': '#ff6347', 'royalblue': '#4169e1', 'sandybrown': '#f4a460', 'steelblue': '#4682b4', 'orchid': '#da70d6', 'limegreen': '#32cd32', 'moccasin': '#ffe4b5', 'cornflowerblue': '#6495ed', 'peachpuff': '#ffdab9', 'darkturquoise': '#00ced1', 'saddlebrown': '#8b4513', 'bisque': '#ffe4c4', 'palegoldenrod': '#eee8aa', 'green': '#008000', 'darkslateblue': '#483d8b', 'lightgreen': '#90ee90', 'indianred': '#cd5c5c', 'orangered': '#ff4500', 'yellowgreen': '#9acd32', 'fuchsia': '#ff00ff', 'lightblue': '#add8e6', 'darkviolet': '#9400d3', 'mediumseagreen': '#3cb371', 'deepskyblue': '#00bfff', 'springgreen': '#00ff7f', 'lightcyan': '#e0ffff', 'brown': '#a52a2a', 'teal': '#008080', 'maroon': '#800000', 'blanchedalmond': '#ffebcd', 'navajowhite': '#ffdead', 'aliceblue': '#f0f8ff', 'darkgray': '#a9a9a9', 'mediumpurple': '#9370db', 'indigo': '#4b0082', 'violet': '#ee82ee', 'orange': '#ffa500', 'sienna': '#a0522d', 'darkslategray': '#2f4f4f', 'navy': '#000080'}
# на январь 2018 здесь на 5 цветов больше чем в википедии