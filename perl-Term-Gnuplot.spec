%define	module	Term-Gnuplot

Name:		perl-%{module}
Version:	0.90380905
Release:	9
Summary:	Lowlevel graphics using gnuplot drawing routines
License:	GPL or Artistic
Group:		Development/Perl
Source0:	http://search.cpan.org/CPAN/modules/by-module/Term/%{module}-%{version}.tar.bz2
Patch0:		Term-Gnuplot-0.90380905-string-format-fix.patch
Url:		http://search.cpan.org/dist/%{module}/
BuildRequires:	perl-devel
BuildRequires:	svgalib-devel
BuildRequires:	gnuplot
Requires:	gnuplot
BuildRequires:	libjpeg-devel
BuildRequires:	X11-devel
BuildRequires:	pkgconfig(libpng15)
BuildRequires:	freetype-devel
buildRequires:	gd-devel

%description
Lowlevel graphics using gnuplot drawing routines.

%prep
%setup -q -n %{module}-%{version}
%patch0 -p1 -b .str_fmt~

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
yes "" | %{__make} test

%install
%makeinstall_std

%files
%doc README
%{_mandir}/*/*
%{perl_vendorlib}/*


%changelog
* Sun Feb 12 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.90380905-9
+ Revision: 773476
- fix typo in string format fix patch
- fix mixed-use-of-spaces-and-tabs
- add 'gd-devel' to buildrequires
- apply string format fix patch
- use pkgconfig() depeendency
- clean up spec
- svn commit -m mass rebuild of perl extension against perl 5.14.2

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.90380905-5mdv2009.0
+ Revision: 258496
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.90380905-4mdv2009.0
+ Revision: 246517
- rebuild

* Tue Jan 15 2008 Thierry Vignaud <tv@mandriva.org> 0.90380905-2mdv2008.1
+ Revision: 152322
- rebuild

* Wed Jan 02 2008 Olivier Blin <blino@mandriva.org> 0.90380905-1mdv2008.1
+ Revision: 140717
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Sun Jan 07 2007 Olivier Thauvin <nanardon@mandriva.org> 0.90380905-1mdv2007.0
+ Revision: 105038
- first mdv package
- Create perl-Term-Gnuplot

