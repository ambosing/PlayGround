using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.AI;

public class TestAgent : MonoBehaviour
{
    private NavMeshAgent _navMeshAgent;
    [SerializeField] private Transform navTargetTransform;

    private void Awake()
    {
        _navMeshAgent = GetComponent<NavMeshAgent>();
    }

    private void Update()
    {
        _navMeshAgent.SetDestination(navTargetTransform.position);
    }
}
