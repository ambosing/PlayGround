using System.Collections;
using System.Collections.Generic;
using UnityEngine;

namespace myBehaviourTree
{
    //------------------------------------------------------------------------------
    // Left Node
    // EBH_Running 존재하지 않음 : EBH_Success or EBH_Failure
    // Initialize(), Terminate() 사용 안함 : 의미 없는 함수 - 조건만 체크하기때문에
    //------------------------------------------------------------------------------

    // 시퀀스 노드에서 제일 처음 접하는 노드
    public class btCondition : btBehaviour
    {
        public btCondition()
        {
            _EnNodeType = enNodeType.Condition;
        }

        public override enStatus Tick()
        {
            _EnStatus = Update();

            if (_EnStatus == enStatus.Running)
            {
                //error
            }

            // !!! (최적화 필요) : 이전 Action node를 참조하는 필드 변수로 만들어 사용
            if (_EnStatus == enStatus.Success)
            {
                // 이전에 다른 노드의 값들을 초기화 하기위해서 - 반드시 들어가는 조건문 필요
                TerminateRunningStatusByOtherAction();
            }

            return _EnStatus;
        }

        public void TerminateRunningStatusByOtherAction()
        {
            btBehaviour btFindRoot = null;
            int IErrorCount = 0;

            // find root
            btFindRoot = _BtParent;
            if (btFindRoot != null)
            {
                while (IErrorCount < 100)
                {
                    btFindRoot = btFindRoot._BtParent;
                    if (btFindRoot._BtParent == null)
                        break;
                    ++IErrorCount;
                }
            }
            // find running action
            if (btFindRoot != null)
            {
                if ((btFindRoot._EnStatus) == enStatus.Running)
                {
                    Debug.Log(btFindRoot is btRoot);
                    btRoot child = ((btRoot)btFindRoot);
                    btBehaviour btRunningAction = FindRunningAction(child.Child);
                    if (btRunningAction != null)
                    {
                        // 만일 this Condition과 Running Action이 같은 부모를 가졌고 해당 부모가 Sequence가 아니라면 Terminate호출
                        if (_BtParent != btRunningAction._BtParent || _BtParent._EnNodeType != enNodeType.Sequence)
                            btRunningAction.Terminate();
                    }
                }
            }
        }
        public btBehaviour FindRunningAction(btBehaviour btChild)
        {
            btBehaviour btRunningAction = null; 

            if (btChild != null)
            {
                if (btChild._EnNodeType == enNodeType.Selector || btChild._EnNodeType == enNodeType.Sequence)
                {
                    for (int i = 0; i < ((btComposite)btChild).GetChildCount(); ++i)
                    {
                        btRunningAction = FindRunningAction(((btComposite)btChild).GetChild(i));
                        if (btRunningAction != null)
                            return btRunningAction;
                    }
                }
                if (btChild._EnNodeType == enNodeType.Action && btChild._EnStatus == enStatus.Running)
                    return btChild;
            }
            return btRunningAction;
        }

    }
}