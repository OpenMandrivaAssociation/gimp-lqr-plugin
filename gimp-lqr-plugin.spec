%define version		0.6.1
%define release		%mkrel 2

%define name		gimp-lqr-plugin
%define gettext_name	gimp20-lqr-plugin

Summary:        Content-aware image resize plug-in for GIMP
Name:           %name
Version:        %version
Release:        %release
License:        GPLv2+
Group:          Graphics
URL:            http://liquidrescale.wikidot.com/
Source0:        http://liquidrescale.wikidot.com/local--files/en:download-page/%{name}-%{version}.tar.bz2
BuildRequires:  gimp-devel >= 2.4
BuildRequires:  liblqr-devel >= 0.3.0
BuildRequires:  intltool
Requires:       gimp >= 2.4
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root

%description
This package is a plug-in for GIMP 2.4. It implements the algorithm
described in the paper "Seam Carving for Content-Aware Image Resizing"
by Shai Avidan and Ariel Shamir, which can be found at
http://www.faculty.idc.ac.il/arik/imret.pdf

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
%find_lang %{gettext_name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{gettext_name}.lang
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog NEWS README TODO
%{_libdir}/gimp/2.0/plug-ins/%{name}
%{_libdir}/gimp/2.0/plug-ins/plug_in_lqr_iter
%{_datadir}/gimp/2.0/scripts/batch-gimp-lqr.scm
%{_datadir}/%{name}
