Name:		texlive-Tabbing
Version:	59715
Release:	2
Summary:	Tabbing with accented letters
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/Tabbing
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tabbing.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tabbing.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tabbing.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
By default, some of the tabbing environment's commands clash
with default accent commands; LaTeX provides the odd commands
\a', etc., to deal with the clash. The package offers a variant
of the tabbing environment which does not create this
difficulty, so that users need not learn two sets of accent
commands.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/tabbing
%doc %{_texmfdistdir}/doc/latex/tabbing
#- source
%doc %{_texmfdistdir}/source/latex/tabbing

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
