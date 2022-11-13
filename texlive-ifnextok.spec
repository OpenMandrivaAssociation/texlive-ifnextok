Name:		texlive-ifnextok
Version:	23379
Release:	1
Summary:	Utility macro: peek ahead without ignoring spaces
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/ifnextok
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ifnextok.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ifnextok.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ifnextok.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package deals with the behaviour of the LaTeX internal
command \@ifnextchar, which skips blank spaces. This has the
potential to surprise users, since it can produce really
unwanted effects. A common example occurs with brackets
starting a line following \\: the command looks for an optional
argument, whereas the user wants the brackets to be printed.
The package offers commands and options for modifying this
behaviour, maybe limited to certain parts of the document
source.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/ifnextok/ifnextok.sty
%doc %{_texmfdistdir}/doc/latex/ifnextok/README
%doc %{_texmfdistdir}/doc/latex/ifnextok/RELEASEs.txt
%doc %{_texmfdistdir}/doc/latex/ifnextok/SRCFILEs.txt
%doc %{_texmfdistdir}/doc/latex/ifnextok/ifnextok.pdf
%doc %{_texmfdistdir}/doc/latex/ifnextok/testIfNT.pdf
#- source
%doc %{_texmfdistdir}/source/latex/ifnextok/ifnextok.tex
%doc %{_texmfdistdir}/source/latex/ifnextok/makedoc.cfg
%doc %{_texmfdistdir}/source/latex/ifnextok/srcfiles.tex
%doc %{_texmfdistdir}/source/latex/ifnextok/testIfNT.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
