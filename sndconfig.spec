Summary:	The Red Hat Linux sound configuration tool
Summary(pl):	Narzêdzie do konfiguracji d¼wiêku
Name:		sndconfig
Version:	0.33
Release:	4
License:	GPL
Group:		Applications/Sound
Source0:	%{name}-%{version}.tar.gz
# Source0-md5:	99735d5aeb239619a47353b6a92b34ef
Patch0:		%{name}-PLD_and_rename_conf.modules.patch.bz2
Patch1:		%{name}-isapnp.patch
Patch2:		%{name}-awe_wave.patch
BuildRequires:	newt-devel
BuildRequires:	slang-devel
%ifarch %{ix86} alpha
Requires:	awesfx
Requires:	isapnptools >= 1.16
Requires:	playmidi
Requires:	sox
Conflicts:	kernel < 2.2.0
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
ExclusiveArch:	%{ix86} sparc alpha

%description
Sndconfig is a text based tool which sets up the configuration files
you'll need to use a sound card with a Red Hat (or compatible) Linux
system. Sndconfig can be used to set the proper sound type for
programs which use the /dev/dsp, /dev/audio and /dev/mixer devices.
The sound settings are saved by the aumix and sysV runlevel scripts.

Install sndconfig if you need to configure your sound card.

%description -l pl
sysconfig jest tekstowym narzêdziem do ustawiania plików
konfiguracyjnych potrzebnych do u¿ywania karty d¼wiêkowej z Linuksem
Red Hata (lub kompatybilnym).

%prep
%setup -q -n %{name}
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__make} RPM_OPT_FLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man8,%{_datadir}/locale}

%{__make} prefix=$RPM_BUILD_ROOT%{_prefix} install
cp $RPM_BUILD_ROOT%{_prefix}/man/man8/* $RPM_BUILD_ROOT%{_mandir}/man8/

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/sndconfig
%ifarch %{ix86} alpha
%attr(755,root,root) %{_sbindir}/pnpprobe
%{_mandir}/man8/pnpprobe.8*
%endif
%dir %{_datadir}/sndconfig
%{_datadir}/sndconfig/sample.au
%{_datadir}/sndconfig/sample.midi
%{_mandir}/man8/sndconfig.8*
