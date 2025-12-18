pkgname = "pihole"
pkgver = "6.4.1"
_webver = "6.2.1"
_scriptver = "6.1.2"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DCMAKE_INSTALL_PREFIX=/usr",
	"-DBUILD_SHARED_LIBS=True",
	"-DCMAKE_BUILD_TYPE=Release",
	"-DPIHOLE_STATE_PATH=/var/lib/pihole",
	"-DPIHOLE_SHARE_PATH=/usr/share/pihole",
	"-DPIHOLE_BIN_PATH=/usr/bin",
	"-DPIHOLE_WEB_PATH=/usr/share/pihole/admin-web",
	"-DPIHOLE_RUN_PATH=/run/pihole",
]
hostmakedepends = ["cmake", "vim-xxd", "ninja", "libcap-progs"]
makedepends = ["dinit-chimera", "libidn2-devel", "readline-devel", "libunistring-devel", "mbedtls-devel", "gmp-devel", "nettle-devel", "linux-headers"]
depends = ["bash", "bind-progs", "ncurses", "curl"]
provides = ["!dnsmasq"]
pkgdesc = "Pi-hole® is a DNS sinkhole that protects your devices"
license = "EUPL-1.2"
url = "https://pi-hole.net"
source = [
    f"https://github.com/pi-hole/FTL/archive/refs/tags/v{pkgver}.tar.gz",
    f"https://github.com/pi-hole/web/archive/refs/tags/v{_webver}.tar.gz",
    f"https://github.com/pi-hole/pi-hole/archive/refs/tags/v{_scriptver}.tar.gz",
]
source_paths = [".", f"web-{_webver}", f"pi-hole-{_scriptver}"]
sha256 = [
    "054da435fc57644d835f6a686a92b77fdff102a6048afdb773c7cc5e8fe48131",
    "89c60c0013efba2865955a890fa6eb32fa4fc5f090a1d9c14a7472fcf3a5c35c",
    "c4d21c6c67a2d2aae3dd0b3bcd50194dfc4995fb2bbf0212731b91199d355296"
]
env = {
    "GIT_BRANCH": "master",
    "GIT_VERSION": f"v{pkgver}",
    "GIT_TAG": f"v{pkgver}",
}
file_modes = {
    "usr/bin/pihole-FTL": ("root", "root", 0o755),
}
file_xattrs = {
    "usr/bin/pihole-FTL": {"security.capability": "cap_net_raw,cap_net_admin,cap_chown,cap_sys_time,cap_net_bind_service+ep"},
}
# no tests
options = []


def install(self):
    self.install_bin("build/pihole-FTL", name="pihole-FTL")
    self.install_bin(f"pi-hole-{_scriptver}/pihole", name="pihole")
    self.install_file(f"pi-hole-{_scriptver}/gravity.sh", "usr/share/pihole/", 0o755)
    self.install_file(f"pi-hole-{_scriptver}/advanced/Scripts/version.sh", "usr/share/pihole/", 0o755)
    self.install_file(f"pi-hole-{_scriptver}/advanced/Scripts/query.sh", "usr/share/pihole/", 0o755)
    self.install_file(f"pi-hole-{_scriptver}/advanced/Scripts/api.sh", "usr/share/pihole/", 0o755)
    self.install_file(f"pi-hole-{_scriptver}/advanced/Scripts/list.sh", "usr/share/pihole/", 0o755)
    self.install_file(f"pi-hole-{_scriptver}/advanced/Scripts/piholeARPTable.sh", "usr/share/pihole/", 0o755)
    self.install_file(f"pi-hole-{_scriptver}/advanced/Scripts/utils.sh", "usr/share/pihole/", 0o755)
    self.install_file(f"pi-hole-{_scriptver}/advanced/Scripts/database_migration/gravity-db.sh", "usr/share/pihole/database_migration/", 0o755)
    self.install_file(f"pi-hole-{_scriptver}/advanced/Scripts/COL_TABLE", "usr/share/pihole/", 0o644)

    self.install_files(f"pi-hole-{_scriptver}/advanced/Scripts/database_migration/gravity/", "usr/share/pihole/database_migration/")
    self.install_files(f"web-{_webver}", "usr/share/pihole/admin-web/", name="admin")

    self.install_file(f"pi-hole-{_scriptver}/advanced/Templates/gravity.db.sql", "usr/share/pihole/templates/", 0o644)
    self.install_file(f"pi-hole-{_scriptver}/advanced/Templates/gravity_copy.sql", "usr/share/pihole/templates/", 0o644)

    self.install_license("LICENSE")

    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
    self.install_sysusers(self.files_path / "sysusers.conf")
    self.install_service(self.files_path / "pihole")
