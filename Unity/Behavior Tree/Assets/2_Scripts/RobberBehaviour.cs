using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.AI;

public class RobberBehaviour : MonoBehaviour
{
    private BehaviourTree tree;
    public GameObject diamond;
    public GameObject van;
    private NavMeshAgent agent;

    private void Start()
    {
        agent = this.GetComponent<NavMeshAgent>();
        
        tree = new BehaviourTree();
        Node steal = new Node("Steal Something");
        Node goToDiamond = new Leaf("Go To Diamond", GoToDiamond);
        Node goToVan = new Leaf("Go To Van", GoToVan);
        
        steal.AddChild(goToDiamond);
        steal.AddChild(goToVan);
        tree.AddChild(steal);
        
        tree.PrintTree();
        tree.Process();
    }

    public Node.Status GoToDiamond()
    {
        agent.SetDestination(diamond.transform.position);
        return Node.Status.SUCCESS;
    }

    public Node.Status GoToVan()
    {
        agent.SetDestination(van.transform.position);
        return Node.Status.SUCCESS;
    }

    private void Update()
    {
        
    }
}
