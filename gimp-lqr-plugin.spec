%global optflags %{optflags} -fno-common

%define gettext_name	gimp20-lqr-plugin

Summary:        Content-aware image resize plug-in for GIMP
Name:           gimp-lqr-plugin
Version:        0.7.2
Release:        1
License:        GPLv2+
Group:          Graphics
URL:            https://liquidrescale.wikidot.com/
Source0:        https://liquidrescale.wikidot.com/local--files/en:download-page/%{name}-%{version}.tar.bz2
BuildRequires:  gimp-devel >= 2.4
BuildRequires:  pkgconfig(lqr-1) >= 0.3.0
BuildRequires:  intltool
Requires:       gimp >= 2.4

%description
This package is a plug-in for GIMP 2.4. It implements the algorithm
described in the paper "Seam Carving for Content-Aware Image Resizing"
by Shai Avidan and Ariel Shamir, which can be found at
http://www.faculty.idc.ac.il/arik/imret.pdf

%prep
%setup -q

%build
%configure
%make_build

%install
%make_install
%find_lang %{gettext_name}

%files -f %{gettext_name}.lang
%doc AUTHORS ChangeLog NEWS README TODO
%{_libdir}/gimp/2.0/plug-ins/%{name}
%{_libdir}/gimp/2.0/plug-ins/plug_in_lqr_iter
%{_datadir}/gimp/2.0/scripts/batch-gimp-lqr.scm
%{_datadir}/%{name}


%changelog
* Wed Nov 16 2011 Götz Waschk <waschk@mandriva.org> 0.7.1-2mdv2012.0
+ Revision: 731093
- rebuild

* Thu Nov 11 2010 Götz Waschk <waschk@mandriva.org> 0.7.1-1mdv2011.0
+ Revision: 595978
- new version

* Fri Jun 04 2010 Lev Givon <lev@mandriva.org> 0.7.0-1mdv2011.0
+ Revision: 547125
- Update to 0.7.0.

* Fri Sep 11 2009 Thierry Vignaud <tv@mandriva.org> 0.6.1-2mdv2010.0
+ Revision: 437693
- rebuild

* Wed Mar 18 2009 Funda Wang <fwang@mandriva.org> 0.6.1-1mdv2009.1
+ Revision: 357140
- New version 0.6.1

* Sat Aug 23 2008 Götz Waschk <waschk@mandriva.org> 0.4.0-1mdv2009.0
+ Revision: 275365
- import gimp-lqr-plugin


* Sat Aug 23 2008 Götz Waschk <waschk@mandriva.org> 0.4.0-1mdv2009.0
- initial package


