pkgname = "cifs-utils"
pkgver = "7.4"
pkgrel = 0
build_style = "configure"
configure_args = []
configure_gen = []
make_dir = "."
hostmakedepends = ["pkgconf", "autoconf", "automake"]
makedepends = [
    "keyutils-devel",
    "libcap-devel",
    "linux-headers",
    "linux-pam-devel",
    "samba-devel",
    "samba-winbind-devel",
    "talloc-devel",
]
checkdepends = []
pkgdesc = "Userspace tools for LinuxCIFS VFS"
license = "GPL-3.0-or-later"
url = "https://wiki.samba.org/index.php/LinuxCIFS_utils"
source = f"https://download.samba.org/pub/linux-cifs/cifs-utils/cifs-utils-{pkgver}.tar.bz2"
sha256 = "53353d05c30b4fc9dac006a8f0c5054cdd8a1834c176313c91e4694025c4b891"
env = {
    "AM_CFLAGS": "",
    "ROOTSBINDIR": "/usr/bin",
}

def configure(self):
    from cbuild.util import gnu_configure

    gnu_configure.replace_guess(self)

    with self.stamp("autogen") as s:
        s.check()
        self.do("autoreconf", "-if")

    self.do("./configure", "--prefix=/usr", "--sbindir=/usr/bin")

# def post_install(self):
#     # config
#     self.install_file(
#         "examples/chrony.conf.example1", "etc", name="chrony.conf"
#     )
#     self.install_sysusers("^/sysusers.conf")
#     self.install_tmpfiles("^/tmpfiles.conf")
#     # dinit services
#     self.install_service("^/chronyd")
#     self.install_service("^/chrony", enable=True)
