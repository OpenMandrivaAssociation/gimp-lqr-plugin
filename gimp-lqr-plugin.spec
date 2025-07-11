%define gettext_name	gimp20-lqr-plugin

Summary:        Content-aware image resize plug-in for GIMP
Name:           gimp-lqr-plugin
Version:        0.7.2
Release:        1
License:        GPLv2+
Group:          Graphics
URL:            https://liquidrescale.wikidot.com/
# Also https://github.com/carlobaldassi/gimp-lqr-plugin
Source0:        https://liquidrescale.wikidot.com/local--files/en:download-page/%{name}-%{version}.tar.bz2
BuildRequires:  gimp-devel >= 2.4
BuildRequires:  pkgconfig(lqr-1) >= 0.3.0
BuildRequires:  intltool
Requires:       gimp >= 2.4
BuildSystem:	autotools

%patchlist
gimp-lqr-plugin-compile.patch

%description
This package is a plug-in for GIMP 2.4. It implements the algorithm
described in the paper "Seam Carving for Content-Aware Image Resizing"
by Shai Avidan and Ariel Shamir, which can be found at
http://www.faculty.idc.ac.il/arik/imret.pdf

%install -a
%find_lang %{gettext_name}

%files -f %{gettext_name}.lang
%doc AUTHORS ChangeLog NEWS README TODO
%{_libdir}/gimp/2.0/plug-ins/%{name}
%{_libdir}/gimp/2.0/plug-ins/plug_in_lqr_iter
%{_datadir}/gimp/2.0/scripts/batch-gimp-lqr.scm
%{_datadir}/%{name}
