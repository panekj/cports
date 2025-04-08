pkgname = "docker"
pkgver = "28.3.3"
pkgrel = 0
build_style = "go"
_commit = "6430e49a55babd9b8f4d08e70ecb2b68900770fe"
make_build_args = ["-mod=vendor", "-modfile=vendor.mod"]
hostmakedepends = [
    "bash",
    "go",
    "go-md2man",
    "linux-headers",
    "pkgconf",
]
depends = ["git", "containerd", "iptables", "procps", "xfsprogs", "xz", "e2fsprogs"]
pkgdesc = "Container and image engine"
license = "Apache-2.0"
url = "https://docker.com"
source = f"https://github.com/moby/moby/archive/v{pkgver}.tar.gz"
sha256 = "3727c8963ab4bcff12291e99e4d4a6b9a29ace5236fd245717bbff648f15f8cd"
env = {
    "AUTO_GOPATH": "1",
    "GITCOMMIT": _commit,
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
    self.env.update(golang.get_go_env(self))


def pre_build(self):
    self.mkdir(self.cwd / "src/github.com/docker", parents=True)
    self.ln_s(self.chroot_cwd, self.cwd / "src/github.com/docker/docker")


def build(self):
    from cbuild.util import golang

    golang.Golang(self).build(args=["github.com/docker/docker/cmd/dockerd"])
    golang.Golang(self).build(args=["github.com/docker/docker/cmd/docker-proxy"])

    self.do("make", wrksrc=self.chroot_cwd / "man")


def install(self):
    dbin = (self.cwd / "build/dockerd").resolve().name
    pbin = (self.cwd / "build/docker-proxy").resolve().name
    self.install_bin(f"build/{dbin}", name="dockerd")
    self.install_bin(f"build/{pbin}", name="docker-proxy")

    self.install_man("man/man8/dockerd.8")

    self.install_service(self.files_path / "dockerd")

    self.install_sysusers(self.files_path / "sysusers.conf")
