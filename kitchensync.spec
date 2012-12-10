Name:		kitchensync
Version:	0.22.0
Release:	2
Summary:	KDE4 OpenSync frontend
Group:		Graphical desktop/KDE
License:	GPLv2+
Url:		http://kde-apps.org/content/show.php/KitchenSync?content=132898
Source:		%{name}-%{version}.tar.bz2
Patch0:		kitchensync-0.22.0-includes.patch
Patch1:		kitchensync-0.22.0-dso.patch
BuildRequires:	kdepimlibs4-devel
BuildRequires:	pkgconfig(opensync-1.0)
BuildRequires:	pkgconfig(osengine-1.0)
Requires:	libopensync-plugin-akonadi

%description
KitchenSync is the KDE frontend to the universal standard syncing
solution OpenSync. It can be used to sync PDAs, mobile phones
or other computers with the KDE desktop and some other applications.

This is the OpenSync 0.22-compatible version.

Authors: Tobias Koenig - Cornelius Schumacher

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

%files
%doc README LICENSE
%{_bindir}/kitchensync
%{_kde_libdir}/kde4/libkitchensyncpart.so
%{_libdir}/libkitchensyncprivate.so.*
%{_libdir}/libqopensync.so*
%{_kde_datadir}/applications/kde4/kitchensync.desktop
%{_kde_iconsdir}/hicolor/*/actions/sync-start.png
%{_kde_iconsdir}/hicolor/*/apps/kitchensync.png
%{_kde_appsdir}/kitchensync

