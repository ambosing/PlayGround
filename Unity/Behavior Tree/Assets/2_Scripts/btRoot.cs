using System.Collections;
using System.Collections.Generic;
using UnityEngine;

namespace myBehaviourTree
{
    public class btRoot : btBehaviour
    {
        private btBehaviour _Child;

        public btBehaviour Child
        {
            get => _Child;
            set => _Child = value;
        }

        public btRoot()
        {
            _EnNodeType = enNodeType.Root;
            _BtParent = null;
        }

        public void AddChild(btBehaviour newChild)
        {
            _Child = newChild;
            _BtParent = this;
        }

        public override void Terminate()
        {
            _Child.Terminate();
            base.Terminate();
        }

        public override enStatus Tick()
        {
            if (_Child == null)
                return enStatus.Invalid;
            else if(_Child._EnStatus == enStatus.Invalid)
            {
                _Child.Initialize();
                _Child._EnStatus = enStatus.Running;
            }
            _EnStatus = _Child.Update();
            _Child._EnStatus = _EnStatus;

            if (_EnStatus != enStatus.Running)
                Terminate();

            return _EnStatus;
        }
    }
}

