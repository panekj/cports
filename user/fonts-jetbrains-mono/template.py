pkgname = "fonts-jetbrains-mono"
pkgver = "2.304"
pkgrel = 0
pkgdesc = "JetBrains Mono typeface family"
license = "OFL-1.1"
url = "https://jetbrains.com/mono"
source = f"https://github.com/JetBrains/JetBrainsMono/releases/download/v{pkgver}/JetBrainsMono-{pkgver}.zip"
sha256 = "6f6376c6ed2960ea8a963cd7387ec9d76e3f629125bc33d1fdcd7eb7012f7bbf"
options = ["empty"]


def install(self):
    self.install_file("fonts/ttf/*.ttf", "usr/share/fonts/JetBrainsMono", glob=True)
    self.install_file("fonts/variable/*.ttf", "usr/share/fonts/JetBrainsMono", glob=True)
    # self.install_file("extras/webfonts/*.otf", "usr/share/fonts/JetBrainsMono", glob=True)
    self.install_license("OFL.txt")


@subpackage("fonts-jetbrains-mono-ttf")
def _(self):
    self.subdesc = "TrueType"
    self.depends = [self.parent]

    return ["usr/share/fonts/JetBrainsMono/*.ttf"]
