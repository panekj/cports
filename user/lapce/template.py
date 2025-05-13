pkgname = "lapce"
pkgver = "0.4.3"
pkgrel = 0
_commit = "adaf8302b13b0ffd4e1bddb30ab8e57e114bf0b4"
# wasmtime
archs = ["aarch64", "x86_64"]
build_style = "cargo"
prepare_after_patch = True
make_build_args = ["--bin", "lapce"]
make_build_env = {
    "RELEASE_TAG_NAME": pkgver,
}
hostmakedepends = [
    "cargo-auditable",
    "cmake",
    "pkgconf",
]
makedepends = [
    "fontconfig-devel",
    "freetype-devel",
    "curl-devel",
    "libgit2-devel",
    "libxkbcommon-devel",
    "rust-bindgen",
    "rust-std",
    "sqlite-devel",
    "zlib-ng-compat-devel",
    "zstd-devel",
]
depends = []
pkgdesc = "Lightning-fast and powerful code editor"
license = "Apache-2.0"
url = "https://lapce.dev"
# fixes vendor
source = f"https://github.com/lapce/lapce/archive/{_commit}.tar.gz"
sha256 = "e37f6c95d93c38292eae5cce219e9906bc27a6501347477273c27d7f8af6496d"
# no
options = ["!check", "!cross"]


def install(self):
    self.install_bin(
        f"target/{self.profile().triplet}/release/lapce",
        name="lapce",
    )
    self.install_file(
        "extra/images/logo.png",
        "usr/share/icons/hicolor/512x512/apps",
        name="dev.lapce.lapce.png",
    )
    self.install_file(
        "extra/linux/dev.lapce.lapce.desktop",
        "usr/share/applications",
        name="dev.lapce.lapce.desktop",
    )
    self.install_file(
        "extra/linux/dev.lapce.lapce.metainfo.xml",
        "usr/share/metainfo",
        name="dev.lapce.lapce.metainfo.xml",
    )
    self.install_license("LICENSE")
