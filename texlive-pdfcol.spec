Name:		texlive-pdfcol
Version:	64469
Release:	2
Summary:	Macros for maintaining colour stacks under pdfTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/pdfcol
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pdfcol.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pdfcol.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pdfcol.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Since version 1.40 pdfTeX supports colour stacks. The driver
file pdftex.def for package color defines and uses a main
colour stack since version v0.04b. This package is intended for
package writers. It defines macros for setting and maintaining
new colour stacks.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/pdfcol
%{_texmfdistdir}/tex/latex/pdfcol
%doc %{_texmfdistdir}/doc/latex/pdfcol

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
