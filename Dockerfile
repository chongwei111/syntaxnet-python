FROM algorithmia/adock-base

ENV SYNTAXNETDIR=/opt/tensorflow PATH=$PATH:/root/bin

RUN mkdir -p $SYNTAXNETDIR \
    && cd $SYNTAXNETDIR \
    && apt-get update \
    && apt-get install git zlib1g-dev file swig python2.7 python-dev -y \
    && conda install protobuf==3.0.0b2 \
    && conda install asciitree \
    && conda install numpy \
    && wget https://github.com/bazelbuild/bazel/releases/download/0.2.2b/bazel-0.2.2b-installer-linux-x86_64.sh \
    && chmod +x bazel-0.2.2b-installer-linux-x86_64.sh \
    && ./bazel-0.2.2b-installer-linux-x86_64.sh --user \
    && git clone --recursive https://github.com/tensorflow/models.git \
    && cd $SYNTAXNETDIR/models/syntaxnet/tensorflow \
    && echo "\n\n\n" | ./configure

RUN cd $SYNTAXNETDIR/models/syntaxnet \
    && bazel build --genrule_strategy=standalone syntaxnet/... util/utf8/... \
    && apt-get autoremove -y \
    && apt-get clean

WORKDIR $SYNTAXNETDIR/models/syntaxnet
