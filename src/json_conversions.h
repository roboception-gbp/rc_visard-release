/*
 * Copyright (c) 2020 Roboception GmbH
 *
 * Author: Elena Gambaro
 *
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions are met:
 *
 * 1. Redistributions of source code must retain the above copyright notice,
 * this list of conditions and the following disclaimer.
 *
 * 2. Redistributions in binary form must reproduce the above copyright notice,
 * this list of conditions and the following disclaimer in the documentation
 * and/or other materials provided with the distribution.
 *
 * 3. Neither the name of the copyright holder nor the names of its contributors
 * may be used to endorse or promote products derived from this software without
 * specific prior written permission.
 *
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
 * AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
 * IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
 * ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
 * LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
 * CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
 * SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
 * INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
 * CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
 * ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
 * POSSIBILITY OF SUCH DAMAGE.
 */

#ifndef RC_TAGDETECT_JSON_CONVERSIONS_H
#define RC_TAGDETECT_JSON_CONVERSIONS_H

#include "json_conversions_common.h"

#include <rc_common_msgs/ReturnCode.h>

#include <rc_tagdetect_client/Tag.h>
#include <rc_tagdetect_client/DetectedTag.h>

#include <rc_tagdetect_client/DetectTags.h>

namespace rc_common_msgs
{
inline void from_json(const nlohmann::json& j, ReturnCode& r)
{
  j.at("value").get_to(r.value);
  j.at("message").get_to(r.message);
}

}  // namespace rc_common_msgs

namespace rc_tagdetect_client
{
inline void to_json(nlohmann::json& j, const Tag& r)
{
  j["id"] = r.id;
  j["size"] = r.size;
}

inline void from_json(const nlohmann::json& j, Tag& r)
{
  j.at("id").get_to(r.id);
  j.at("size").get_to(r.size);
}

inline void from_json(const nlohmann::json& j, DetectedTag& r)
{
  j.at("timestamp").get_to(r.header.stamp);
  j.at("pose_frame").get_to(r.header.frame_id);
  j.at("id").get_to(r.tag.id);
  j.at("size").get_to(r.tag.size);
  j.at("instance_id").get_to(r.instance_id);
  j.at("pose").get_to(r.pose.pose);
  r.pose.header.stamp = r.header.stamp;
  r.pose.header.frame_id = r.header.frame_id;
}

inline void to_json(nlohmann::json& j, const DetectTagsRequest& r)
{
  j["tags"] = r.tags;
  if (!r.pose_frame.empty())
  {
    j["pose_frame"] = r.pose_frame;
    if (r.pose_frame == "external")
    {
      j["robot_pose"] = r.robot_pose;
    }
  }
}

inline void from_json(const nlohmann::json& j, DetectTagsResponse& r)
{
  j.at("tags").get_to(r.tags);
  j.at("timestamp").get_to(r.timestamp);
  j.at("return_code").get_to(r.return_code);
}

}  // namespace rc_tagdetect_client

#endif  // RC_TAGDETECT_JSON_CONVERSIONS_H
