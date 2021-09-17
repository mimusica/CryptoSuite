FROM ubuntu:20.04

LABEL org.opencontainers.image.source=https://github.com/mimusica/CryptoSuite
LABEL Maintainer=Christophe@Langenberg.be
LABEL version=0.1
LABEL Description="This a multistage dockerfile that contains all the needs to deploy our CryptoSuite."

ENV TZ=Europe/Madrid

USER 0

COPY . /opt/CryptoSuite/

WORKDIR /opt/CryptoSuite/

    # Set our timezone
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime \
    && echo $TZ > /etc/timezone \
    # suppress interactive messages
#    && DEBIAN_FRONTEND="noninteractive" \
    # check for new updates and install them
    && apt-get update \
    && apt-get upgrade -y \
    && apt-get dist-upgrade -y \
    # installing the additional software packages that we will need
    && apt-get install -y --no-install-recommends \
                python3-pip \
                ca-certificates \
                file \
                libexpat1 \
                libmagic-mgc \
                libmagic1 \
                libpython3.9-minimal \
                libpython3.9-stdlib \
                libreadline8 \
                libsqlite3-0 \
                libssl1.1 \
                mime-support \
                openssl \
                python3.9 \
                python3.9-minimal \
                readline-common \
                tzdata \
                xz-utils \
    # clean up
    && apt-get autoremove -y \
    && apt-get clean autoclean \
    && rm -rf /var/lib/apt/lists/* \
    && pip3 install --upgrade pip \
    && pip3 install --no-cache-dir -r requirements.txt


#CMD [ "python3", "cryptosuite.py" ]