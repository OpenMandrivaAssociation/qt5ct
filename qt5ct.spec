%define debug_package %{nil}
#
# spec file for package qt5ct
#

Name:           qt5ct
Version:        0.22
Release:        1
Summary:        Qt5 Configuration Tool
License:        BSD-2-Clause
Group:          Graphical desktop/Other
Url:            http://opendesktop.org/content/show.php/qt5ct?content=168066
Source:        %name-%version.tar.bz2
Source1:		qt5ct.desktop
#---------------------------------------------------------
BuildRequires: qmake5
BuildRequires: qt5-linguist-tools
BuildRequires: qtchooser
BuildRequires: qt5-devel
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Gui)
BuildRequires: pkgconfig(Qt5Multimedia)
BuildRequires: pkgconfig(Qt5MultimediaWidgets)
BuildRequires: pkgconfig(Qt5Widgets)

%description
This applications allows users to configure Qt5 settings (theme,
font, icons, etc.) under DE/WM without Qt integration.

%prep
%setup -q

%build
qmake-qt5
%make

%install
rm -rf %buildroot
make install INSTALL_ROOT=%{buildroot}

#install fixed desktop file
install -m 0644 %SOURCE1 %{buildroot}%{_datadir}/applications/qt5ct.desktop
  
%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING README TODO
%_bindir/qt5ct
%{_libdir}/qt5/plugins/platformthemes/libqt5ct.so
%{_datadir}/applications/qt5ct.desktop


%changelog
* Sun May 17 2015 bb <bb> 0.11-1pclos2015
- create package for pclos
