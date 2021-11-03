using System.Collections;
using System.Collections.Generic;
using UnityEngine;

namespace myBehaviourTree
{
    public class btComposite : btBehaviour
    {
        protected List<btBehaviour> _listChild;

        public btComposite()
        {
            _listChild = new List<btBehaviour>();
        }

        public btBehaviour GetChild(int idx)
        {
            return _listChild[idx];
        }

        public int GetChildCount()
        {
            return _listChild.Count;
        }

        public override void Reset()
        {
            for (int i = 0; i < GetChildCount(); i++)
            {
                GetChild(i).Reset();
            }
        }

        public void AddChild(btBehaviour newChild)
        {
            _listChild.Add(newChild);
            newChild.IIndex = _listChild.Count - 1;
            newChild._BtParent = this;
        }
    }

}


