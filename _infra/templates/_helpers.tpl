{{- /*
Generate a name that combines the release name and chart name to make it unique
*/ -}}
{{- define "flask-api.fullname" -}}
{{- printf "%s-%s" .Release.Name .Chart.Name | trunc 63 | trimSuffix "-" -}}
{{- end -}}

{{- /*
Generate a short name for the chart
*/ -}}
{{- define "flask-api.name" -}}
{{- .Chart.Name | trunc 63 | trimSuffix "-" -}}
{{- end -}}

{{- /*
Generate a namespace-specific name for the chart
*/ -}}
{{- define "flask-api.namespace" -}}
{{- printf "%s-%s" .Release.Namespace .Chart.Name | trunc 63 | trimSuffix "-" -}}
{{- end -}}
