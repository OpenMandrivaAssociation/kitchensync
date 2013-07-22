%define major 4
%define libkitchensyncprivate %mklibname kitchensyncprivate %{major}
%define libqopensync %mklibname qopensync %{major}

Summary:	KDE4 OpenSync frontend
Name:		kitchensync
Version:	0.22.0
Release:	3
Group:		Graphical desktop/KDE
License:	GPLv2+
Url:		http://kde-apps.org/content/show.php/KitchenSync?content=132898
Source0:	%{name}-%{version}.tar.bz2
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

%files
%doc README LICENSE
%{_bindir}/kitchensync
%{_kde_appsdir}/kitchensync
%{_kde_applicationsdir}/kitchensync.desktop
%{_kde_libdir}/kde4/libkitchensyncpart.so
%{_kde_iconsdir}/hicolor/*/actions/sync-start.png
%{_kde_iconsdir}/hicolor/*/apps/kitchensync.png

#----------------------------------------------------------------------------

%package -n %{libkitchensyncprivate}
Summary:	Shared library for KitchenSync
Group:		System/Libraries
Conflicts:	%{name} < 0.22.0-3

%description -n %{libkitchensyncprivate}
Shared library for KitchenSync.

%files -n %{libkitchensyncprivate}
%{_kde_libdir}/libkitchensyncprivate.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{libqopensync}
Summary:	Shared library for KitchenSync
Group:		System/Libraries
Conflicts:	%{name} < 0.22.0-3

%description -n %{libqopensync}
Shared library for KitchenSync.

%files -n %{libqopensync}
%{_kde_libdir}/libqopensync.so.%{major}*

#----------------------------------------------------------------------------

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

# We don't need this because there are no headers anyway
rm -f %{buildroot}%{_kde_libdir}/libqopensync.so

