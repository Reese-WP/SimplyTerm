class Tile:

    _last_style = None
    _last_export = ""
    _style_history = {}

    def __init__(
        self,
        char = "",
        foreground: str | None = None,
        background: str | None = None,
        bold =False,
        dim =False,
        italic = False,
        underline = False,
        blink = False,
        reverse = False,
        hidden = False,
        strikethrough = False
    ):
        self.char = char
        self.foreground = foreground
        self.background = background
        self.bold = bold
        self.dim = dim
        self.italic = italic
        self.underline = underline
        self.blink = blink
        self.reverse = reverse
        self.hidden = hidden
        self.strikethrough = strikethrough

    def export(self):

        #checks if last exported tile had the same colors/style and if so skips the exporting to save a bit of time
        state = self._get_style_state()

        if state == Tile._last_style:
            return ""
        
        if state in Tile._style_history:
            export_code = Tile._style_history[state]

            Tile._last_style = state
            Tile._last_export = export_code

            return export_code

        
        codes = []

        if self.bold:
            codes.append("1")
        if self.dim:
            codes.append("2")
        if self.italic:
            codes.append("3")
        if self.underline:
            codes.append("4")
        if self.blink:
            codes.append("5")
        if self.reverse:
            codes.append("7")
        if self.hidden:
            codes.append("8")
        if self.strikethrough:
            codes.append("9")

        def _extract_code(seq):
            if not isinstance(seq, str):
                return None
            if seq.startswith("\x1b[") and seq.endswith("m"):
                return seq[2:-1]
            return None

        def _extract_color(hex_color, background=False):
            if not isinstance(hex_color, str):
                return None
            if hex_color.startswith("#"):
                hex_color = hex_color[1:]
            if len(hex_color) != 6:
                return None

            try:
                r = int(hex_color[0:2], 16)
                g = int(hex_color[2:4], 16)
                b = int(hex_color[4:6], 16)
            except ValueError:
                return None

            color_type = "48" if background else "38"
            return f"{color_type};2;{r};{g};{b}"            

        foreground_code = _extract_color(self.foreground)
        background_code = _extract_color(self.background, background=True)

        if foreground_code:
            codes.append(foreground_code)
        if background_code:
            codes.append(background_code)

        if not codes:
            return ""

        export_code = "\x1b[" + ";".join(codes) + "m"

        Tile._style_history[state] = export_code
        Tile._last_style = state
        Tile._last_export = export_code

        return export_code

    def copy(self):
        return Tile(
            char=self.char,
            foreground=self.foreground,
            background=self.background,
            bold=self.bold,
            dim=self.dim,
            italic=self.italic,
            underline=self.underline,
            blink=self.blink,
            reverse=self.reverse,
            hidden=self.hidden,
            strikethrough=self.strikethrough
        )

    def _get_style_state(self):
        return (
            self.foreground,
            self.background,
            self.bold,
            self.dim,
            self.italic,
            self.underline,
            self.blink,
            self.reverse,
            self.hidden,
            self.strikethrough
    )

    def __eq__(self, other):
        if not isinstance(other, Tile):
            return NotImplemented

        return (
            self.char == other.char
            and self.foreground == other.foreground
            and self.background == other.background
            and self.bold == other.bold
            and self.dim == other.dim
            and self.italic == other.italic
            and self.underline == other.underline
            and self.blink == other.blink
            and self.reverse == other.reverse
            and self.hidden == other.hidden
            and self.strikethrough == other.strikethrough
        )