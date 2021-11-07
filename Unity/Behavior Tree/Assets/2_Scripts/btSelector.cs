using System.Collections;
using System.Collections.Generic;
using UnityEngine;

namespace myBehaviourTree
{
    public class btSeletor : btComposite
    {
        public btSeletor()
        {
            _EnNodeType = enNodeType.Selector;
        }

        public override enStatus Update()
        {
            for (int i = 0; i < GetChildCount(); ++i)
            {
                enStatus enCurrentStatus = GetChild(i).Tick();

                if (enCurrentStatus != enStatus.Failure)
                {
                    ClearChild(i);
                    return enCurrentStatus;
                }
            }

            return enStatus.Failure;
        }

        // 자식 중 EBH_Success or EBH_Running를 발견하면 모든 자식을 초기화(이때, 기존의 EBH_Running이 있으면 Terminatied()함수 호출)
        protected void ClearChild(int iSkipIndex)
        {
            for (int i = 0; i < GetChildCount(); ++i)
            {
                if (i != iSkipIndex)
                {
                    GetChild(i).Reset();
                }
            }
        }
    }
}
