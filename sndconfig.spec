Summary:	The Red Hat Linux sound configuration tool
Summary(pl):	Narzêdzie do konfiguracji d¼wiêku
Name:		sndconfig
Version:	0.33
Release:	1
License:	GPL
Group:		Applications/Multimedia
######		Unknown group!
Source0:	%{name}-%{PACKAGE_VERSION}.tar.gz
%ifarch i386 alpha
Requires:	isapnptools >= 1.16, sox, awesfx, playmidi, kernel >= 2.2.0
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
ExclusiveArch:	%{ix86} sparc alpha

%description
Sndconfig is a text based tool which sets up the configuration files
you'll need to use a sound card with a Red Hat Linux system. Sndconfig
can be used to set the proper sound type for programs which use the
/dev/dsp, /dev/audio and /dev/mixer devices. The sound settings are
saved by the aumix and sysV runlevel scripts.

Install sndconfig if you need to configure your sound card.

%prep
%setup -q -n sndconfig

%build
%{__make} RPM_OPT_FLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man8,%{_datadir}/locale}

%{__make} prefix=$RPM_BUILD_ROOT%{_prefix} install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/sndconfig
%ifarch %{ix86} alpha
%attr(755,root,root) %{_sbindir}/pnpprobe
%{_mandir}/man8/pnpprobe.8*
%endif
%{_datadir}/sndconfig/sample.au
%{_datadir}/sndconfig/sample.midi
%{_datadir}/locale/*/*/sndconfig.mo
%{_mandir}/man8/sndconfig.8*
