pkgname = "git-credential-oauth"
pkgver = "0.15.0"
pkgrel = 0
build_style = "go"
make_dir = "bin"  # needed for tests
make_build_args = [
    "-ldflags=-X github.com/hickford/git-credential-oauth/main.version={pkgver}"
]
hostmakedepends = ["go"]
checkdepends = []
depends = ["git"]
pkgdesc = "Git credential helper that securely authenticates using OAuth"
license = "Apache-2.0"
url = "https://github.com/hickford/git-credential-oauth"
source = f"https://github.com/hickford/git-credential-oauth/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "c9b067fde5849b597aceba15b76c5b9ccacee4e5736e88c9ae430553bb7f2898"
# a test fails after go bump
options = []


def post_build(self):
    self.mkdir("man")


def check(self):
    from cbuild.util import golang

    self.golang.check()


def install(self):
    self.install_bin("bin/git-credential-oauth")
    self.install_license("LICENSE.txt")
    self.install_man("git-credential-oauth.1")
