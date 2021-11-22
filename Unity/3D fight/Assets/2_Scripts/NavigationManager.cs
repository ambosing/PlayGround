using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.AI;

public class NavigationManager : MonoBehaviour
{
    private NavMeshSurface[] _surfaces;

    private void Awake()
    {
        _surfaces = FindObjectsOfType<NavMeshSurface>();
    }

    private void Update()
    {
        // if (Input.GetKeyDown())
    }

    private void BackSurface()
    {
        foreach (var navMeshSurface in _surfaces)
        {
            navMeshSurface.BuildNavMesh();
        }
    }
}
