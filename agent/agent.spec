Name:     agent
Version:  0.0.5
Release:  1
Summary:  The HTTP api Agent
License:  GPLv3+
URL:      http://yum.inside.mts.by/agent
Source:  %{name}-%(version).tgz
Packager: Maksim Astapenko
Source1:  agent.yml
Source2:  agent.service
Source3:  agent

%description
The HTTP api Agent for manage daemons.

%prep

%build

%install
mkdir -p %{buildroot}/var/spool/%{name}/{dhcp,samba,smtp,squid,techmail}
touch %{buildroot}/var/spool/%{name}/dhcp/dhcpd.conf.head
touch %{buildroot}/var/spool/%{name}/dhcp/dhcpd.conf.recv
touch %{buildroot}/var/spool/%{name}/samba/smb.conf.head
touch %{buildroot}/var/spool/%{name}/samba/smb.conf.recv
mkdir -p %{buildroot}/etc/agent
cp -p %{SOURCE1} %{buildroot}/etc/agent/
mkdir -p %{buildroot}/usr/lib/systemd/system/
cp -p %{SOURCE2} %{buildroot}/usr/lib/systemd/system/
mkdir -p %{buildroot}/usr/sbin/
cp -p %{SOURCE3} %{buildroot}/usr/sbin/

%post
case "$1" in
 1)
  # install
   /usr/bin/systemctl daemon-reload
  ;;

 2)
  # upgrade
   /usr/bin/systemctl restart agent.service
  ;;
esac

%preun
if [ $1 = 0 ]; then
    /usr/bin/systemctl stop agent.service
    /usr/bin/systemctl disable agent.service
fi

%files
%dir %{_localstatedir}/spool/agent/smtp
%dir %{_localstatedir}/spool/agent/squid
%dir %{_localstatedir}/spool/agent/techmail
%config(noreplace) %{_sysconfdir}/agent/agent.yml
%config(noreplace) %{_localstatedir}/spool/%{name}/dhcp/dhcpd.conf.head
%config(noreplace) %{_localstatedir}/spool/%{name}/dhcp/dhcpd.conf.recv
%config(noreplace) %{_localstatedir}/spool/%{name}/samba/smb.conf.head
%config(noreplace) %{_localstatedir}/spool/%{name}/samba/smb.conf.recv
%defattr(0755,root,root)
%{_sbindir}/agent
%defattr(0644,root,root)
/usr/lib/systemd/system/agent.service

%clean

%changelog
* Thu Sep 23 2021 ma@mts.by 0.0.5
- Bug fix snapshot backup method. 8fd86de
* Thu Sep 22 2021 ma@mts.by 0.0.4
- Add zfs snapshot backup method. Code refactor. 20cb181
* Thu Mar 19 2021 ma@mts.by 0.0.3
- Add missed smtp forward update. 2a528b6
* Thu Feb 11 2021 ma@mts.by 0.0.2
- Add multi type json for parse request. 2bf0192
* Sat Jan 25 2021 ma@mts.by 0.0.1
- Initial version of the package
