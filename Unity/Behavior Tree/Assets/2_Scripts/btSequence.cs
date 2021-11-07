using System.Collections;
using System.Collections.Generic;
using UnityEngine;

namespace myBehaviourTree
{
    public class btSequence : btComposite
    {
        public btSequence()
        {
            _EnNodeType = enNodeType.Sequence;
        }

        public override enStatus Update()
        {
            enStatus enCurrentStatus = enStatus.Invalid;

            for (int i = 0; i < GetChildCount(); i++)
            {
                // ?? status ?? ?? ???
                enCurrentStatus = GetChild(i)._EnStatus;

                if (GetChild(i)._EnNodeType != enNodeType.Action || GetChild(i)._EnStatus != enStatus.Success)
                    enCurrentStatus = GetChild(i).Tick();

                if (enCurrentStatus != enStatus.Success)
                    return enCurrentStatus;
            }
            return enStatus.Success;
        }
    }
}