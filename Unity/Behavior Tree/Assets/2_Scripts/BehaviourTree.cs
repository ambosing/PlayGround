using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class BehaviourTree : Node
{
    public BehaviourTree()
    {
        name = "Tree";
    }

    public BehaviourTree(string name)
    {
        this.name = name;
    }

    public override Status Process()
    {
        return children[currentChild].Process();
    }

    public struct NodeLevel
    {
        public int level;
        public Node node;
    }
    

    public void PrintTree()
    {

        string treePrintout = "";
        Stack<NodeLevel> nodeStack = new Stack<NodeLevel>();
        Node currentNode = this;
        nodeStack.Push(new NodeLevel{level = 0, node = currentNode});
        
        while (nodeStack.Count != 0)
        {
            NodeLevel nextNode = nodeStack.Pop();
            treePrintout += new string('-' ,nextNode.level) + nextNode.node.name + "\n";
            for (int i = nextNode.node.children.Count - 1; i >= 0; i--)
            {
                nodeStack.Push(new NodeLevel {level = nextNode.level + 1, node = nextNode.node.children[i]});
            }
        }
        // Dfs(ref treePrintout, nodeStack);
        Debug.Log(treePrintout);
    }

    // public void Dfs(ref string treePrintout,Stack<NodeLevel> nodeStack )
    // {
    //     if (nodeStack.Count == 0)
    //         return;
    //     NodeLevel nextNode = nodeStack.Pop();
    //     treePrintout += new string('-' ,nextNode.level) + nextNode.node.name + "\n";
    //     for (int i = 0; i < nextNode.node.children.Count; i++)
    //     {
    //         Debug.Log("Dfs 실행함2" + "\t" + treePrintout);
    //         nodeStack.Push(new NodeLevel {level = nextNode.level + 1, node = nextNode.node.children[i]});
    //         Dfs(ref treePrintout, nodeStack);
    //     }
    // }
}
