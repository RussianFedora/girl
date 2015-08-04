Name:          girl
Version:       6.0.0
Release:       3%{?dist}
Summary:       GNOME Internet Radio Locator

License:       GPLv2+
URL:           https://wiki.gnome.org/Apps/Girl
Source0:       https://download.gnome.org/sources/girl/6.0/%{name}-%{version}.tar.xz
# https://bugzilla.gnome.org/show_bug.cgi?id=753044
Patch0:        0001-trivial-update-FSF-address.patch

# for autosetup -S git
BuildRequires: git-core
# main deps
BuildRequires: gcc
BuildRequires: pkgconfig(gtk+-2.0)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(libgnomeui-2.0)
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: pkgconfig(gnome-vfs-2.0)
BuildRequires: pkgconfig(libgnome-2.0)
BuildRequires: intltool
BuildRequires: itstool
# check
BuildRequires: /usr/bin/desktop-file-validate
BuildRequires: /usr/bin/appstream-util

Requires:      streamripper
Requires:      totem

%description
GIRL is a GNOME Internet Radio Locator program that allows the user
to easily find and record live radio programs on radio broadcasters
on the Internet.

GIRL is developed on the GNOME platform and it requires at least
one audio player such as Videos to be installed for playback and
streamripper for recording.

%prep
%autosetup -S git

%build
%configure
%make_build

%install
%make_install

%find_lang %{name}

%check
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/appdata/%{name}.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%post
update-desktop-database &> /dev/null || :
touch --no-create %{_datadir}/icons/hicolor &> /dev/null || :

%postun
update-desktop-database &> /dev/null || :
if [ $1 -eq 0 ] ; then
    touch --no-create %{_datadir}/icons/hicolor &> /dev/null || :
    gtk-update-icon-cache %{_datadir}/icons/hicolor &> /dev/null || :
fi

%posttrans
gtk-update-icon-cache %{_datadir}/icons/hicolor &> /dev/null || :

%files -f %{name}.lang
%license COPYING
%doc AUTHORS LETTER NEWS README TODO VERSION YP-DIRS ChangeLog
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_mandir}/man1/%{name}.1*
%{_datadir}/help/*/%{name}/*

%changelog
* Tue Aug 04 2015 Maxim Orlov <murmansksity@gmail.com> - 6.0.0-3
- Changing release number
- Add BuildRequires: pkgconfig(libgnome-2.0)

* Mon Aug 03 2015 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 6.0.0-2
- Fixes many issues and cleanups in spec

* Mon Aug  3 2015 Maxim Orlov <murmansksity@gmail.com> - 6.0.0-1
- Initial package.
