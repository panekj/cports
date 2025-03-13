pkgname = "docker-credential-helpers"
pkgver = "0.9.2"
pkgrel = 0
build_style = "makefile"
make_build_args = [f"VERSION={pkgver}", f"REVISION=''", "build-secretservice", "build-pass"]
hostmakedepends = [
    "go",
    "pkgconf",
]
makedepends = [
    "libsecret-devel",
]
depends = []
go_build_tags = []
pkgdesc = "Programs to keep Docker login credentials safe"
license = "MIT"
url = "https://github.com/docker/docker-credential-helpers"
source = (
    f"https://github.com/docker/docker-credential-helpers/archive/refs/tags/v{pkgver}.tar.gz"
)
sha256 = "bdad4f712244f11dc64890db2f915166306bb4b040149f4497c31f33c7a87327"
# needs subid config in the chroot
options = ["!check", "empty"]

def install(self):
    self.install_file(
        f"{self.make_dir}/bin/build/docker-credential-pass",
        "usr/bin",
        name="docker-credential-pass",
    )
    self.install_file(
        f"{self.make_dir}/bin/build/docker-credential-secretservice",
        "usr/bin",
        name="docker-credential-secretservice",
    )
    self.install_license(f"{self.make_dir}/LICENSE")


@subpackage("docker-credential-pass")
def _(self):
    self.pkgdesc = "Containerd benchmarking utility"
    self.install_if = [self.parent, self.with_pkgver("docker-cli"), self.with_pkgver("pass")]

    return ["usr/bin/docker-credential-pass"]


@subpackage("docker-credential-secretservice")
def _(self):
    self.pkgdesc = "Containerd benchmarking utility"
    self.install_if = [self.parent, self.with_pkgver("docker-cli"), self.with_pkgver("gnome-keyring")]

    return ["usr/bin/docker-credential-secretservice"]
