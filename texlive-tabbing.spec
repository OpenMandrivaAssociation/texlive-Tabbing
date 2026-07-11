%global tl_name tabbing
%global tl_revision 78931

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Tabbing with accented letters
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/Tabbing
License:	lppl1
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tabbing.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tabbing.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tabbing.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
By default, some of the tabbing environment's commands clash with
default accent commands; LaTeX provides the odd commands \a', etc., to
deal with the clash. The package offers a variant of the tabbing
environment which does not create this difficulty, so that users need
not learn two sets of accent commands.

