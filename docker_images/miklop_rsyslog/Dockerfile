FROM alpine

RUN apk add --no-cache \
	rsyslog \
	logrotate

COPY rsyslog.conf /etc/
COPY miklop /etc/logrotate.d/
COPY start_syslog_cron /usr/local/bin/start_syslog_cron

RUN chmod +x /usr/local/bin/start_syslog_cron


EXPOSE 514/udp

CMD /usr/local/bin/start_syslog_cron

