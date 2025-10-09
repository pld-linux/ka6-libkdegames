#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeappsver	25.08.2
%define		qtver		5.15.2
%define		kaname		libkdegames
Summary:	Libkdegames
Name:		ka6-%{kaname}
Version:	25.08.2
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	d345a82fe43d3ebb6116fae25fa1de8d
URL:		http://www.kde.org/
BuildRequires:	OpenAL-devel
BuildRequires:	Qt6Core-devel
BuildRequires:	Qt6Core-devel >= %{qtver}
BuildRequires:	Qt6Gui-devel >= 5.11.1
BuildRequires:	Qt6Network-devel >= 5.11.1
BuildRequires:	Qt6Qml-devel
BuildRequires:	Qt6Quick-devel
BuildRequires:	Qt6Svg-devel
BuildRequires:	Qt6Test-devel
BuildRequires:	Qt6Widgets-devel
BuildRequires:	cmake >= 3.20
BuildRequires:	gettext-devel
BuildRequires:	kf6-extra-cmake-modules >= 5.53.0
BuildRequires:	kf6-karchive-devel
BuildRequires:	kf6-kbookmarks-devel
BuildRequires:	kf6-kcodecs-devel
BuildRequires:	kf6-kcompletion-devel
BuildRequires:	kf6-kconfig-devel
BuildRequires:	kf6-kconfigwidgets-devel
BuildRequires:	kf6-kcoreaddons-devel
BuildRequires:	kf6-kcrash-devel
BuildRequires:	kf6-kdbusaddons-devel
BuildRequires:	kf6-kdeclarative-devel
BuildRequires:	kf6-kdnssd-devel
BuildRequires:	kf6-kglobalaccel-devel
BuildRequires:	kf6-kguiaddons-devel
BuildRequires:	kf6-ki18n-devel
BuildRequires:	kf6-kiconthemes-devel
BuildRequires:	kf6-kio-devel
BuildRequires:	kf6-kitemviews-devel
BuildRequires:	kf6-kjobwidgets-devel
BuildRequires:	kf6-knewstuff-devel
BuildRequires:	kf6-kservice-devel
BuildRequires:	kf6-ktextwidgets-devel
BuildRequires:	kf6-kwidgetsaddons-devel
BuildRequires:	kf6-kxmlgui-devel
BuildRequires:	libsndfile-devel
BuildRequires:	ninja
BuildRequires:	qt6-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
%requires_eq_to Qt6Core Qt6Core-devel
Obsoletes:	ka5-%{kaname} < %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Base library common to many KDE games.

%description -l pl.UTF-8
Bazowa biblioteka wspólna dla wielu gier KDE.

%package devel
Summary:	Header files for %{kaname} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{kaname}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	ka5-%{kaname}-devel < %{version}

%description devel
Header files for %{kaname} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{kaname}.

%prep
%setup -q -n %{kaname}-%{version}

%build
%cmake \
	-B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DKDE_INSTALL_DOCBUNDLEDIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON
%ninja_build -C build

%if %{with tests}
ctest --test-dir build
%endif


%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%ghost %{_libdir}/libKDEGames6.so.6
%attr(755,root,root) %{_libdir}/libKDEGames6.so.*.*
%ghost %{_libdir}/libKDEGames6Private.so.6
%attr(755,root,root) %{_libdir}/libKDEGames6Private.so.*.*
%dir %{_libdir}/qt6/qml/org/kde/games
%dir %{_libdir}/qt6/qml/org/kde/games/core
%{_libdir}/qt6/qml/org/kde/games/core/KGameItem.qml
%{_libdir}/qt6/qml/org/kde/games/core/corebindingsplugin.qmltypes
%{_libdir}/qt6/qml/org/kde/games/core/kde-qmlmodule.version
%attr(755,root,root) %{_libdir}/qt6/qml/org/kde/games/core/libcorebindingsplugin.so
%{_libdir}/qt6/qml/org/kde/games/core/qmldir
%{_datadir}/carddecks
%{_datadir}/qlogging-categories6/libkdegames.categories

%files devel
%defattr(644,root,root,755)
%{_includedir}/KDEGames6
%{_libdir}/cmake/KDEGames6
%{_libdir}/libKDEGames6.so
%{_libdir}/libKDEGames6Private.so
