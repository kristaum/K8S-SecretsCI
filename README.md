# README #

Idea to have secrets managed on a separated repository, this gives more security on dealing with K8S secrets.


Jenkins will use the files here to make secret updates on cluster. On this case we have two cluster a QA and Prod cluster.


The file name will be composed by 3 variables:

* namespace

* secret name

* file name that needs to be sent to K8S

{namespace} _ {secret name} _ {file name}


Sample Name convention:

dotnet_log4net-servico_log4net.config
