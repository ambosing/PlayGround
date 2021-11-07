using System.Collections;
using System.Collections.Generic;
using UnityEngine;

namespace myBehaviourTree
{
    //------------------------------------------------------------------------------
    // Left Node
    // Actor의 상태를 처리하는 클래스
    // * 해당 Action Node가 EBH_Success 상태고 재방문 시 skip
    //------------------------------------------------------------------------------

    public class btAction : btBehaviour
    {
        public btAction()
        {
            _EnNodeType = enNodeType.Action;
        }
        public override void Initialize() { }

        public override void Terminate() { }

        public override void Reset()
        {
            _EnStatus = enStatus.Invalid;
        }

        public override enStatus Tick()
        {
            if (_EnStatus == enStatus.Invalid)
            {
                Initialize();
                _EnStatus = enStatus.Running;
            }
            _EnStatus = Update();
            

            if (_EnStatus != enStatus.Running)
                Terminate();

            return _EnStatus;
        }
    }
}
