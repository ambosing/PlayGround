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
    public GameObject backdoor;
    public GameObject frontdoor;
    // public GameObject point;
    private NavMeshAgent agent;

    public enum ActionState
    {
        IDLE,
        WORKING
    };

    private ActionState state = ActionState.IDLE;

    private Node.Status treeStatus = Node.Status.RUNNING;

    private void Start()
    {
        agent = this.GetComponent<NavMeshAgent>();
        
        tree = new BehaviourTree();
        Sequence steal = new Sequence("Steal Something");
        // Node goToPoint = new Leaf("Go To Point", GoToPoint);
        Node goToFrontDoor = new Leaf("Go To FrontDoor", GoToFrontDoor);
        Node goToBackDoor = new Leaf("Go To BackDoor", GoToBackDoor);
        Node goToDiamond = new Leaf("Go To Diamond", GoToDiamond);
        Node goToVan = new Leaf("Go To Van", GoToVan);
        Selector openDoor = new Selector("Open Door");
        
        openDoor.AddChild(goToFrontDoor);
        openDoor.AddChild(goToBackDoor);
        
        //steal.AddChild(goToPoint);
        steal.AddChild(openDoor);
        steal.AddChild(goToFrontDoor);
        //steal.AddChild(goToBackDoor);
        steal.AddChild(goToDiamond);
        //steal.AddChild(goToBackDoor);
        steal.AddChild(goToVan);
        
        tree.AddChild(steal);
        
        tree.PrintTree();
    }

    private Node.Status GoToFrontDoor()
    {
        return GoToDoor(frontdoor);
    }

    // public Node.Status GoToPoint()
    // {
    //     return GoToLocation(point.transform.position);
    // }

    public Node.Status GoToBackDoor()
    {
        return GoToDoor(backdoor);
    }

    public Node.Status GoToDiamond()
    {
        return GoToLocation(diamond.transform.position);
    }

    public Node.Status GoToVan()
    {
        return GoToLocation(van.transform.position);
    }

    public Node.Status GoToDoor(GameObject door)
    {
        Node.Status status = GoToLocation(door.transform.position);
        if (status == Node.Status.SUCCESS)
        {
            if (!door.GetComponent<Lock>().isLocked)
            {
                door.SetActive(false);
                return Node.Status.SUCCESS;
            }

            return Node.Status.FAILURE;
        }
        else
            return status;
    }

    Node.Status GoToLocation(Vector3 destination)
    {
        float distanceToTarget = Vector3.Distance(destination, this.transform.position);
        if (state == ActionState.IDLE)
        {
            agent.SetDestination(destination);
            state = ActionState.WORKING;
        }
        else if (Vector3.Distance(agent.pathEndPosition, destination) >= 2)
        {
            state = ActionState.IDLE;
            return Node.Status.FAILURE;
        }
        else if (distanceToTarget < 2)
        {
            state = ActionState.IDLE;
            return Node.Status.SUCCESS;
        }

        return Node.Status.RUNNING;
    }

    private void Update()
    {
        if (treeStatus == Node.Status.RUNNING)
            treeStatus = tree.Process();
    }
}
