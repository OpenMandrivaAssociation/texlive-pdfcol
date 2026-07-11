%global tl_name pdfcol
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.8
Release:	%{tl_revision}.1
Summary:	Macros for maintaining colour stacks under pdfTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/pdfcol
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pdfcol.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pdfcol.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pdfcol.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Since version 1.40 pdfTeX supports colour stacks. The driver file
pdftex.def for package color defines and uses a main colour stack since
version v0.04b. This package is intended for package writers. It defines
macros for setting and maintaining new colour stacks.

