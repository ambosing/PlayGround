using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.AI;

public class PlayerMove : MonoBehaviour
{

    private NavMeshAgent agent;
    private Animator _animator;
    private static readonly int HashTrace = Animator.StringToHash("Trace");
    private static readonly int Attack = Animator.StringToHash("Attack");

    private void Start()
    {
        agent = GetComponent<NavMeshAgent>();
        _animator = GetComponent<Animator>();
        StartCoroutine(Test());
    }

    private void Update()
    {
        // if (agent.remainingDistance >= 2.0f)
        // {
        //     Vector3 direction = agent.desiredVelocity;
        //     Quaternion lookRotation = Quaternion.LookRotation(direction);
        //     transform.rotation = Quaternion.Slerp(transform.rotation, lookRotation, 0.05f);
        // }
    }

    private IEnumerator Test()
    {
        while (true)
        {
            Collider[] colls = Physics.OverlapSphere(transform.position, 15f);
            foreach (var coll in colls)
            {
                float dis = Vector3.Distance(transform.position, coll.transform.position);
                if (coll.CompareTag("Player"))
                {
                    print(dis + "\t" + colls.Length);

                    if (dis > 2f)
                    {
                        MoveToTarget(coll.transform);
                    }
                    else
                    {
                        agent.isStopped = true;
                        agent.updatePosition = false;
                        agent.updateRotation = false;
                        agent.velocity = Vector3.zero;
                        _animator.SetBool(HashTrace, false);
                        StartCoroutine(CheckAnimationState());
                    }
                    
                }
            }
            yield return new WaitForSeconds(0.1f);
        }
    }

    private void OnDrawGizmos()
    {
        Gizmos.color = new Color(0.5f, 0.5f, 0.5f, 0.5f);
        Gizmos.DrawSphere(transform.position, 15f);
    }

    private IEnumerator CheckAnimationState()
    {

        while (_animator.GetCurrentAnimatorStateInfo(0).normalizedTime
               < 0.8f)
            yield return null;
        _animator.SetTrigger(Attack);

    }

    private void MoveToTarget(Transform targetTr)
    {
        Debug.Log("aa");
        agent.isStopped = false;
        agent.updatePosition = true;
        agent.updateRotation = true;
        _animator.SetBool(HashTrace, true);
        agent.SetDestination(targetTr.position);
    }
}
