pkgname = "packer"
pkgver = "1.12.0"
pkgrel = 0
build_style = "go"
# _commit = "6430e49a55babd9b8f4d08e70ecb2b68900770fe"
# make_build_args = []
hostmakedepends = [
    # "bash",
    "go",
    # "go-md2man",
    # "pkgconf",
    # "linux-headers",
]
depends = []
pkgdesc = "Tool for creating machine images for multiple platforms"
license = "BUSL-1.1"
url = "https://hashicorp.com/packer"
source = f"https://github.com/hashicorp/packer/archive/v{pkgver}.tar.gz"
sha256 = "29555343555a5786568ea7599a98977b6185b43c3efb0f45d09d1c93d559433a"
env = {
    "AUTO_GOPATH": "1",
#    "GITCOMMIT": _commit,
    "VERSION": pkgver,
    "DISABLE_WARN_OUTSIDE_CONTAINER": "1",
    "GO_MD2MAN": "go-md2man",
}
# nah
options = ["!check"]


def init_build(self):
    from cbuild.util import golang

    self.env["GOPATH"] = str(self.chroot_cwd)
    self.env["GOBIN"] = str(self.chroot_cwd / "bin")
    self.env["CGO_ENABLED"] = "1"
    self.env["GO111MODULE"] = "on"
    self.env["GOTOOLCHAIN"] = "local"
    self.env["GOLDFLAGS"] = f"-X github.com/hashicorp/packer/version.Version={pkgver} -X github.com/hashicorp/packer/version.VersionPrerelease="
    self.env.update(golang.get_go_env(self))


def install(self):
    self.install_bin(f"build/packer", name="packer")
