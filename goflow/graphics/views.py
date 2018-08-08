#!/usr/local/bin/python
# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponseRedirect

from goflow.graphics.models import Graph
from goflow.workflow.models import Process


def graph(request, id, template='goflow/graphics/graph.html'):
    processes = Process.objects.all()
    graph = Graph.objects.get(id=(int(id)))
    return render(request, template, {'processes':processes, 'graph':graph})


def graph_save(request, id):
    # save positions TODO
    return HttpResponseRedirect('..')
