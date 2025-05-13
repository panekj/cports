pkgname = "traefik"
pkgver = "3.4.0"
pkgrel = 0
build_style = "go"
make_build_args = ["-ldflags", f"-s -w -X github.com/traefik/traefik/v3/pkg/version.Codename=cheddar -X github.com/traefik/traefik/v3/pkg/version.Version={pkgver}", "./cmd/traefik"]
hostmakedepends = ["go"]
makedepends = []
checkdepends = []
pkgdesc = "Cloud native application proxy"
license = "MIT"
url = "https://traefik.io"
source = f"https://github.com/traefik/traefik/releases/download/v{pkgver}/traefik-v{pkgver}.src.tar.gz"
sha256 = "da5dcdbf177c5008a157e4180b039a34a7ad10b710a9ce999545ac86d7c217e4"
# generates completions with host binary
options = ["!check"]


def post_install(self):
    self.install_sysusers(self.files_path / "sysusers.conf")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
    self.install_service(self.files_path / "traefik")

    self.install_license("LICENSE.md")
