pkgname = "package-version-server"
pkgver = "0.0.7"
pkgrel = 0
# zed
archs = ["aarch64", "x86_64"]
build_style = "cargo"
prepare_after_patch = True
make_build_args = []
make_build_env = {
    # "RELEASE_VERSION": pkgver,
    # "ZED_UPDATE_EXPLANATION": "Managed by system package manager",
}
hostmakedepends = [
    "cargo-auditable",
    "pkgconf",
]
makedepends = [
    "rust-std",
    "openssl3-devel",
]
depends = []
pkgdesc = "Language server that handles hover information in package.json files"
license = "MIT"
url = "https://github.com/zed-industries/package-version-server"
source = (
    f"https://github.com/zed-industries/package-version-server/archive/refs/tags/v{pkgver}.tar.gz"
)
sha256 = "67ceab7068a50eb79aa3c5721189f5471d12637af5973ce83b3531a8a4d198fa"
# # workaround code that fails with default gc-sections with lld
# # https://github.com/zed-industries/zed/issues/15902
# tool_flags = {"RUSTFLAGS": ["-Clink-arg=-Wl,-z,nostart-stop-gc"]}
# no
options = ["!check", "!cross"]


def install(self):
    self.install_bin(
        f"target/{self.profile().triplet}/release/package-version-server",
        name="package-version-server",
    )
    self.install_license("README.md")
