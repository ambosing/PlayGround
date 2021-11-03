using System.Collections;
using System.Collections.Generic;
using UnityEngine;

namespace myBehaviourTree
{
    public enum enStatus
    {
        Invalid,
        Success,
        Failure,
        Running,
        Aborted

    }
    public enum enNodeType
    {
        Root,
        Selector,
        Sequence,
        Paraller,
        Decorator,
        Condition,
        Action
    }


    public class btBehaviour
    {
        private enStatus _enStatus;
        private enNodeType _enNodeType;
        private int _iIndex;
        private btBehaviour _btParent;

        public btBehaviour _BtParent
        {
            get => _btParent;
            set => _btParent = value;
        }

        public enStatus _EnStatus
        {
            get => _enStatus;
            set => _enStatus = value;
        }

        public enNodeType _EnNodeType
        {
            get => _enNodeType;
            set => _enNodeType = value;
        }

        public int IIndex
        {
            get => _iIndex;
            set => _iIndex = value;
        }

        public btBehaviour()
        {
            _enStatus = enStatus.Invalid;
        }

        public bool IsTerminated()
        {
            return _enStatus == enStatus.Success | _enStatus == enStatus.Failure;
        }

        public bool IsRunning()
        {
            return _enStatus == enStatus.Running;
        }

        virtual public void Reset()
        {
            _enStatus = enStatus.Invalid;
        }

        public virtual enStatus Update()
        {
            return enStatus.Success;
        }

        public virtual void Initialize()
        {

        }

        public virtual void Terminate()
        {

        }

        public virtual enStatus Tick()
        {
            if (_enStatus == enStatus.Invalid)
            {
                Initialize();
                _enStatus = enStatus.Running;
            }
            _enStatus = Update();

            if (_enStatus != enStatus.Running)
            {
                Terminate();
            }

            return _enStatus;
        }
    }
}